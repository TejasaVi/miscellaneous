#!/usr/bin/python

import argparse
import glob
import stat
import sys
import os
BASE_PATH = '/var/log'


def search_logs(path=BASE_PATH):
    for item in glob.glob(path + '/*'):
        if os.path.isdir(item):
            search_logs(os.path.join(path,item))
        else:
            try:
                print item, oct(stat.S_IMODE(os.lstat(item).st_mode))
            except:
                print "Failure: XXX"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',"--path", required=False)
    args = parser.parse_args()
    if not args.path:
        args.path = BASE_PATH
    search_logs(args.path)

if __name__ == '__main__':
    sys.exit(main())
