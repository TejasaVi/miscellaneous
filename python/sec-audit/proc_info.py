#!/usr/bin/python

import psutil
import sys

def main():
    for proc in psutil.process_iter():
        try:
            print proc.as_dict(attrs=['pid', 'username', 'name'])
        except psutil.NoSuchProcess:
            pass

if __name__ == '__main__':
    sys.exit(main())
