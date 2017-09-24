CC= cc
CFLAGS= -Wall -c
EXTRAS= -pthread -lrt -luuid

OBJS= qbuffer.c  qbuffer.h

qbuffer: qbuffer.c  qbuffer.h
	$(CC) qbuffer.c -o $@
clean:
	rm -rf sbuf_user *.o *.gch
