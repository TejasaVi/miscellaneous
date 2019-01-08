#!/bin/bash

gcc -W -Wall -O3 -fpic -fPIC -c libforkmonitor.c
gcc -shared -Wl,-soname,libforkmonitor.so libforkmonitor.o -ldl -o libforkmonitor.so
gcc -W -Wall -O3 forkmonitor.c -o forkmonitor
#./forkmonitor "$PWD/commsocket"
#env "LD_PRELOAD=$PWD/libforkmonitor.so" "FORKMONITOR_SOCKET=$PWD/commsocket" sh -c 'date ; ls -laF'

