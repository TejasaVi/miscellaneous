#!/usr/bin/python

"""

This script checks for open ports and list the executable location for the port
with PIDs

"""

import psutil
import socket

rows = []
lc = psutil.net_connections('inet')
for c in lc:
    (ip, port) = c.laddr
    if ip == '0.0.0.0' or ip == '::':
        if c.type == socket.SOCK_STREAM and c.status == psutil.CONN_LISTEN:
            proto_s = 'tcp'
        elif c.type == socket.SOCK_DGRAM:
            proto_s = 'udp'
        else:
            continue
        proc_exe =''
        for proc in psutil.process_iter():
            if proc.pid == c.pid:
                proc_exe = proc.exe()
        pid_s = str(c.pid) if c.pid else '(unknown)'
        msg = 'PID {} is listening on port {}/{} for all IPs.\n\tThe executable location is at:{}\n'
        msg = msg.format(pid_s, port, proto_s,proc_exe)
        print(msg)
