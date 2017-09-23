#include <stdio.h>
#include <stdlib.h>


typedef struct Q_data {
	int data;
	struct Q_data *nxt;
}data;

typedef struct Queue {
	int max_size;
	int counter;
	data *ptr_front;
	data *ptr_end;
}Q;



/*Functions for a Queue */
int enqueue(Q *q, int input);
int dequeue(Q *q);

void print_queue(Q *q);
int peek(Q *q);
int isEmpty(Q *q);
int isFull(Q *q);
int intialize(Q *q, int size);
