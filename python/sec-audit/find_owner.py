#!/bin/python

import os
from pwd import getpwuid
import sys
import argparse
import glob

BASE_PATH = "/"
"""
def find_owner(filename):
    return getpwuid(stat(filename).st_uid).pw_name
"""

def find_owner(filename):
    if filename:
        st = os.stat(filename)
        userinfo = getpwuid(st.st_uid)
        return getpwuid(st.st_uid).pw_name
    else:
        return None

def find_perms_of_files(filename):
    return

def find_files_for_user(path, user="root"):
    for item in glob.glob(path + '/*'):
        if os.path.isdir(item):
            find_files_for_user(user,os.path.join(path,item))
        elif os.path.islink(item):
            continue
        else:
            owner = find_owner(item)
            if owner == user:
                print item
                
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',"--path", required=True)
    parser.add_argument('-u',"--user", required=False)
    args = parser.parse_args()
    if not args.user:
        args.path = 'root'
    find_files_for_user(args.path, args.user) 

if __name__ == "__main__":
    sys.exit(main())
