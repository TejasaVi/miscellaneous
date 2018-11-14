''' script to manage the File Permissions in Hardening '''
import os
import stat
from pwd import getpwuid


class PremissionsHandler(object):
    ''' Class to manage the file Permissions in Hardening '''

    def __init__(self):
        ''' Init function '''
        self.__loc = None
        self.default_perm = 0
        self.current_perm = 0
        self.owner = None
        self.hardened = 0

    def initialize(self, name):
        ''' Named Initialization function '''
        self.__loc = name
        self.current_perm = self.default_perm = self.get_permission()
        self.owner = self.get_owner()

    def get_permission(self):
        ''' Gets the File Permissions '''
        try:
            if os.path.exists(self.__loc):
                return oct(os.stat(self.__loc)[stat.ST_MODE])[-4:]
            else:
                return -1
        except OSError:
            print("Could not check file default permissions")
            return -1

    def get_owner(self):
        ''' Gets the File Owner '''
        return getpwuid(os.stat(self.__loc).st_uid).pw_name

    def change_permission(self, new_perms):
        ''' Changes the File Permissions '''
        os.chmod(self.__loc, new_perms)
        self.current_perms = self.get_permission()

    def __repr__(self):
        ''' Prints the Class Object content '''
        return "[{0}, {1}, {2}, {3}, {4}]".format(self.__loc, self.default_perm, self.current_perm, self.owner, self.hardened)

if __name__ == "__main__":
    obj = PremissionsHandler()
    print obj
    import pdb
    #pdb.set_trace()
    obj.initialize("tp.txt")
    print obj
    obj.change_permission(0444)
    print obj
