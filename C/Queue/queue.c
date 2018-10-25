#include <stdio.h>
#include <malloc.h>
#include "queue.h"

Q* createQ(int size){
	Q *q = malloc(sizeof(Q));
	q->front = q->end = NULL;
	q->size = size;
	return q;
}

void enQueue(struct Queue *q, int k){

	node *tmp = malloc(sizeof(node));
	tmp->bufferID = k;
	tmp->next = NULL;
	if(q->end ==NULL){
		q->front = q->end = tmp;
		return;
	}
	else{
		q->end->next = tmp;
		q->end = tmp;
	}
}

node* deQueue(struct Queue *q){

    if (q->front == NULL)
       return NULL;

	node *tmp = q->front;
	q->front = q->front->next;
	if (q->front == NULL){
		q->end= NULL;
	}
	return tmp;
}

void printQueue(Q *q){
	if  (q->front != NULL){
		node *tmp = q->front;
		while(tmp != q->end){
			printf("<%d>",tmp->bufferID);
			tmp = tmp->next;
		}
	}
	printf("\n");
	return;
}

int main()
{
    Q *q = createQ(10);
    enQueue(q, 10);
    enQueue(q, 20);
	printQueue(q);
    deQueue(q);
    deQueue(q);
	printQueue(q);
    enQueue(q, 30);
    enQueue(q, 40);
    enQueue(q, 50);
	printQueue(q);
    node *n = deQueue(q);
    if (n != NULL)
      printf("Dequeued item is %d\n", n->bufferID);
	printQueue(q);
    return 0;
}
