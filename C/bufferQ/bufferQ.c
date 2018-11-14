
int writeBuffer(Q *q){
	node  *tmp;

}

int readBuffer(Q *q){
}


Q* createQ(int size){
    Q *q = malloc(sizeof(Q));
    q->front = q->end = NULL;
    q->size = size;
    return q;
}

static int count;
void enQueue(struct Queue *q){

    node *tmp = malloc(sizeof(node));
    tmp->bufferID = count++;
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

void deQueue(struct Queue *q){

    if (q->front == NULL)
       return NULL;

    node *tmp = q->front;
    q->front = q->front->next;
    if (q->front == NULL){
        q->end= NULL;
    }
    free(tmp);
}

