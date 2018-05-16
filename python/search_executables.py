#!/bin/python 

"""Checks for all the executable files on system. """

import argparse
import stat
import os
import glob
import sys

BASE_PATH = "/"
START_PATH = ""


def check_executable_files_recursively(path=BASE_PATH):
    for item in glob.glob(path+'/*'):
        if os.path.isdir(item):
                check_executable_files_recursively(os.path.join(path,item))
        else:
            try:
                if stat.S_IXUSR & os.stat(item)[stat.ST_MODE]:
                    print item, "is executable by its owner"
                else:
                    print item, "is not an executable file"
            except:
                print "Failure: XXX"
                

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',"--path", required=False)
    args = parser.parse_args()
    import pdb;pdb.set_trace()
    if not args.path:
        args.path = BASE_PATH
    check_executable_files_recursively(args.path)
    #else:
    #    check_executable_files_recursively()

if __name__ == "__main__":
    sys.exit(main())
