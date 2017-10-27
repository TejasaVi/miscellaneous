import unittest
import os

def convert_to_dict(data):
    cfg_dict = {}
    data = data.splitlines()
    for line in data:
        if len(line.split()) >2:
            continue
        key,value = line.split()
        if not cfg_dict.has_key(key):
            cfg_dict[key] = (value)
        else:
            orig_value = cfg_dict[key]
            if isinstance(orig_value,type([])):
                cfg_dict[key].append(value)
            else:
                cfg_dict[key] = [orig_value]
                cfg_dict[key] += [value]
    return cfg_dict

TEST_CFG_LOCATION = '/tmp/dummy_sshd_config'
class TestSSHSuit(unittest.TestCase):
    def test_sshd_config_env(self):
        self.assertTrue(os.path.exists('/root/.ssh/'))

    def test_sshd_config_exits(self):
        self.assertTrue(os.path.exists('/etc/ssh/sshd_config'))

    def test_sshd_config_perm(self):
        import stat
        st = os.stat('/etc/ssh/sshd_config')
        self.assertEqual(oct(st.st_mode)[-3:], str(600))

    def test_sshd_nologin_file_exits(self):
        self.assertFalse(os.path.exists('/etc/nologin'))

    def test_sshd_port(self):
        self.assertTrue(self.cfg['port'],"22")

    def test_sshd_protocol(self):
        self.assertTrue(self.cfg['protocol'],"2")

    def test_sshd_AllowUsers(self):
        self.assertTrue(self.cfg.has_key('allowusers'))
        print("Implicitly allowed Users: %s" %self.cfg['allowusers'])

    def test_sshd_DenyUsers(self):
        self.assertTrue(self.cfg.has_key('denyusers'))
        print("Implicitly Denied Users: %s" %self.cfg['denyusers'])

    def test_sshd_idle_logout_timeout_interval(self):
        self.assertEqual(self.cfg['clientaliveinterval'],"300")
        self.assertEqual(self.cfg['clientalivecountmax'], "0")

    def test_sshd_disable_rhosts(self):
        self.assertTrue(self.cfg['ignorerhosts'], "yes")

    def test_sshd_HostbasedAuthentication(self):
        self.assertTrue(self.cfg['hostbasedauthentication'], "no")

    def test_sshd_PermitRootLogin(self):
        self.assertTrue(self.cfg['permitrootlogin'], "no")

    def test_sshd_PermitEmptyPasswords(self):
        self.assertTrue(self.cfg['permitemptypasswords'], "no")

    def test_sshd_X11Forwarding(self):
        self.assertTrue(self.cfg['x11forwarding'], "no")

    def test_sshd_DNShostname(self):
        self.assertTrue(self.cfg['usedns'],"yes")

    def test_sshd_MaxAuthTries(self):
        self.assertTrue(self.cfg['maxauthtries'],"6")

    def test_sshd_PubkeyAuthentication(self):
        self.assertTrue(self.cfg['pubkeyauthentication'],"yes")

    def test_sshd_PermitTunnel(self):
        self.assertTrue(self.cfg['permittunnel'],"no")

    def test_sshd_IgnoreUserKnownHosts(self):
        self.assertTrue(self.cfg['ignoreuserknownhosts'],"no")

    def test_sshd_ListenAddress(self):
        self.assertTrue(self.cfg.has_key('listenaddress'))
        self.assertNotEqual(str(self.cfg['listenaddress']),"['0.0.0.0:22', '[::]:22']")
        print('ssh is listening at %s' %self.cfg['listenaddress'])

    def test_sshd_LoginGraceTime(self):
        self.assertEqual(self.cfg['logingracetime'],"120")

    def test_sshd_PasswordAuthentication(self):
        self.assertTrue(self.cfg['passwordauthentication'],"yes")

    def test_sshd_RSAAuthentication(self):
        self.assertTrue(self.cfg['rsaauthentication'],"yes")

    def test_sshd_hosts_allow(self):
        self.assertTrue(os.path.exists('/etc/hosts.allow'))

    def test_sshd_hosts_deny(self):
        self.assertTrue(os.path.exists('/etc/hosts.deny'))

    def test_sshd_RhostsRSAAuthentication(self):
        self.assertTrue(self.cfg['rhostsrsaauthentication'],"yes")

    def test_sshd_StrictModes(self):
        self.assertTrue(self.cfg['strictmodes'],"yes")

    def test_sshd_addressfamily(self):
        self.assertTrue(self.cfg.has_key('addressfamily'))
        self.assertFalse(self.cfg['addressfamily'],"any")
        print("sshd is listening for explicitly %s" % self.cfg['addressfamily'])

    def test_sshd_allowagentforwarding(self):
        self.assertTrue(self.cfg['allowagentforwarding'],"no")

    def test_sshd_allowstreamlocalforwarding(self):
        self.assertTrue(self.cfg['allowstreamlocalforwarding'],"no")

    def test_sshd_allowtcpforwarding(self):
        self.assertTrue(self.cfg['allowtcpforwarding'],"no")

    def test_sshd_authorizedkeysfile(self):
        self.assertTrue(self.cfg['authorizedkeysfile'],".ssh/authorized_keys")

    def test_sshd_challengeresponseauthentication(self):
        self.assertTrue(self.cfg['challengeresponseauthentication'],"yes")

    def test_sshd_ciphers(self):
        #check for weak ciphers
        return

    def test_sshd_macs(self):
        # check for weak macs
        return

    def test_sshd_kexalgorithms(self):
        # check for weak algos
        return

    def test_sshd_loglevel(self):
        self.assertTrue(self.cfg['loglevel'],"DEBUG")

    def test_sshd_fingerprinthash(self):
        self.assertTrue(self.cfg['fingerprinthash'],"SHA256")


    def setUp(self):
        # copy config_file to some location
        with open('/etc/ssh/sshd_config',"r") as r_fd:
            _file_content = r_fd.read()
        with open(TEST_CFG_LOCATION,'w') as w_fd:
            w_fd.write(_file_content)
        #read the config and pass to the test.
        import subprocess
        p = subprocess.Popen(["sshd", "-T", "-f", "/etc/ssh/sshd_config"], stdout=subprocess.PIPE)
        if not p.returncode:
            result = p.communicate()[0]
            self.cfg = convert_to_dict(result)

    def tearDown(self):
        #delete dummy config_file at location created
        os.remove(TEST_CFG_LOCATION)

if __name__ == '__main__':
    unittest.main()
