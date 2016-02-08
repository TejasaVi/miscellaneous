import logging
from datetime import datetime

class log:
    hostname = ""
    clientname = ""
    version = ""
    user = ""

    def __init__(host,client,version,user):
        self.hostname = host
        self.clientname = client
        self.version =version
        self.user= user
    

    def print_log(msg):
        print time

now = datetime.now()
print '\n\n[%s:%s:%s] [%s] := This is the Log Message ' %(now.hour,now.minute,now.second,'DEBUG')
