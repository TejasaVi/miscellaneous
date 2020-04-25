CC= cc
DEBUG= -g
LIB= -c
CFLAGS= -Wall $(DEBUG)
EXTRALIB= -lpthread
OUT= thread_pid


all:	thread_pid

thread_pid: thread_pid.c
	$(CC) $(CFLAGS) $(EXTRALIB) thread_pid.c -o $@
	chmod +x $@
clean:
	rm -rf $(OUT)
