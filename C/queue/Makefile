CC = cc
CFLAGS = -Wall -c
DEBUG = -g
OBJ = queue.o




runnable: runnable.c $(OBJ)
	$(CC) runnable.c $(OBJ) -o runnable

queue.o: queue.c queue.h
	$(CC) $(CFLAGS) queue.c
clean:
	rm -rf runnable *.o
