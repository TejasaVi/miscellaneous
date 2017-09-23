#include <stdio.h>
#include <stdlib.h>
#include "queue.h"


int enqueue(Q *q, int input)
{
	if(isFull(q)){
		printf("Queue is Full\n");
		return -1;
	}
	else {
		printf("Inserting data into the Queue\n");
		data *tmp = malloc(sizeof(data));
		tmp->data = input;
		tmp->nxt = NULL;
		if(isEmpty(q)){
			//q->ptr_front = tmp;
			q->ptr_end = q->ptr_front = tmp;
			q->counter+=1;
			return 0;
		}
		else{
			q->ptr_end->nxt = tmp;
			q->ptr_end = tmp;
			q->counter+=1;
			return 0;
		}
		
	}
	
	return -1;
}

int dequeue(Q *q)
{
	if(isEmpty(q)) {
		printf("No elements to dequeue\n");
		return -1;
	}
	else{
		data *tmp = q->ptr_front;
		int out = peek(q);
		q->ptr_front = q->ptr_front->nxt;
		free(tmp);
		q->counter -=1;
		return out;
	}
	return -1;
}

void print_queue(Q *q){
	data *tmp= q->ptr_front;
	for(int i=0; i< q->counter;i++){
		printf("[%d] ", tmp->data );
		tmp = tmp->nxt; 
	}
	printf("\n");
}


int peek(Q *q)
{
	if(!isEmpty(q)){
		return q->ptr_front->data;
	}
	else{
		printf("Queue is Empty on Element to peek\n");
		return -1;
	}
}

int isEmpty(Q *q)
{
	if (q->counter == 0)
		return 1;
	return 0;
}

int isFull(Q *q)
{
	if(q->max_size == q->counter)
		return 1;
	return 0;
}

int intialize(Q *q, int size)
{
	if (size < 1){
		printf("Initialization failed least size of Queue should be 1\n");
		return -1;
	}	
	q->max_size = size;
	q->counter =0;
	printf("Initialized New Queue\n");
	return 1;
}
