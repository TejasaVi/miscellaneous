#!/bin/sh -e


USER_ADDED_TO_LXD_GROUP="${USER}"
export GOPATH=${HOME}/go

# Setup subuid and subgid.
echo "root:100000:65536" | sudo tee -a /etc/subuid
echo "root:100000:65536" | sudo tee -a /etc/subgid

# LXD/LXC uses lxc-xxx pakcage.
sudo dnf install -y lxc-devel

# The container-selinux has supported LXD.
sudo dnf install -y container-selinux

# Add lxd group and add user to lxd group.
sudo /usr/sbin/groupadd -r lxd
sudo gpasswd -a "${USER_ADDED_TO_LXD_GROUP}" lxd
sudo mkdir /var/lib/lxd
sudo chown root:lxd /var/lib/lxd
sudo restorecon /var/lib/lxd

# Build LXD and install LXD.
sudo dnf install -y git golang sqlite-devel dnsmasq squashfs-tools libacl-devel
go get -v -x github.com/lxc/lxd/lxc github.com/lxc/lxd/lxd
sudo cp "${GOPATH}"/bin/lxd /usr/bin
sudo chown root:lxd /usr/bin/lxd
sudo restorecon /usr/bin/lxd
sudo cp "${GOPATH}"/bin/lxc /usr/bin
sudo chown root:lxd /usr/bin/lxc
sudo restorecon /usr/bin/lxc

# Create LXD directory.
sudo mkdir -p /var/log/lxd
sudo chown root:lxd /var/log/lxd
sudo restorecon /var/log/lxd

# Setup systemd service.
cat <<EOF | sudo tee /usr/lib/systemd/system/lxd.service
[Unit]
Description=LXD - main daemon
After=network.target
Requires=network.target lxd.socket
Documentation=man:lxd(1)

[Service]
Environment="LXD_SOCKET=/var/run/lxd/unix.socket"
EnvironmentFile=-/etc/environment
ExecStart=/usr/bin/lxd --group lxd --logfile=/var/log/lxd/lxd.log
ExecStartPost=/usr/bin/lxd waitready --timeout=600
KillMode=process
TimeoutStartSec=600
TimeoutStopSec=40
Restart=on-failure
LimitNOFILE=infinity
LimitNPROC=infinity

[Install]
Also=lxd.socket
EOF
sudo restorecon /usr/lib/systemd/system/lxd.service
cat <<EOF | sudo tee /usr/lib/systemd/system/lxd.socket
[Unit]
Description=LXD - unix socket
Documentation=man:lxd(1)

[Socket]
ListenStream=/var/run/lxd/unix.socket
SocketGroup=lxd
SocketMode=0660
Service=lxd.service

[Install]
WantedBy=sockets.target
EOF
sudo restorecon /usr/lib/systemd/system/lxd.socket
sudo systemctl --system daemon-reload
sudo systemctl enable lxd.service

cat <<EOF | sudo tee /etc/profile.d/lxd.sh
export LXD_SOCKET=/var/run/lxd/unix.socket
EOF

# Setup kernel.
sudo dnf install -y grub2-tools
# shellcheck disable=SC1091
. /etc/default/grub
C="user_namespace.enable=1 namespace.unpriv_enable=1"
C="$GRUB_CMDLINE_LINUX $C"
sudo sed -e "s;^GRUB_CMDLINE_LINUX=.*;GRUB_CMDLINE_LINUX=\"$C\";g" \
     -i /etc/default/grub
sudo /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg
cat <<EOF | sudo tee /etc/sysctl.d/lxd.conf
user.max_user_namespaces=15076
EOF

# LXD can be used after reboot.
sudo /sbin/reboot
