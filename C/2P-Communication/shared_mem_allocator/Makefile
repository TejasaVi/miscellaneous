CC= cc
CFLAGS= -Wall -c
EXTRAS= -pthread -lrt -luuid

OBJS= shared_mem_allocator.h shared_mem_allocator.c

sbuf_user: shared_mem_allocator.o usage.c
	$(CC) usage.c shared_mem_allocator.o $(EXTRAS) -o $@

sbuf_allocator.o: $(OBJS) 
	$(CC) $(OBJS) $(CFLAGS)

clean:
	rm -rf sbuf_user *.o *.gch
