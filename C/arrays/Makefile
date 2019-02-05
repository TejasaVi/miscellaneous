CC = cc
CFLAGS = -Wall -c
DEBUG = -g

all: lib_array.o runner.c
	$(CC) runner.c lib_array.o -o runner
lib_array.o: lib_array.c lib_array.h
	$(CC) $(CFLAGS) lib_array.c

clean:
	rm -rf lib_array.o runner
