#!/usr/bin/python

import pwd, grp
import pprint
import sys

mappings = {}

def main():
    for p in pwd.getpwall():
        if grp.getgrgid(p[3])[0] not in mappings.keys():
            mappings[grp.getgrgid(p[3])[0]] = [p[0]]
        else:
            mappings[grp.getgrgid(p[3])[0]].append(p[0])
    pprint.pprint(mappings)

if __name__ == '__main__':
    sys.exit(main())

