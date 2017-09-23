CC= cc
CFLAGS= -Wall -c
EXTRAS= -pthread -lrt

OBJS= shared_mutex.c  shared_mutex.h 

smutexer: shared_mutex.o usage.c
	$(CC) usage.c shared_mutex.o $(EXTRAS) -o $@

sbuf_allocator.o: $(OBJS) 
	$(CC) $(OBJS) $(CFLAGS)

clean:
	rm -rf smutexer *.o *.gch
