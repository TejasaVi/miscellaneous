# --- macros
CC=cc
LIBS = -lrt -lpthread

all: producer consumer

producer: producer.c common.c
	$(CC) producer.c common.c -o producer $(LIBS)

consumer: consumer.c common.c
	$(CC) consumer.c common.c -o consumer $(LIBS)

clean:
	rm -rf consumer producer
