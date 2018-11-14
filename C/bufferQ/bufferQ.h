

typedef struct Qnode{
	//char buf_name[10];
	int bufferID;
	struct Qnode *next;
}node;



typedef struct Queue{
	int size;
	node *front, *end;
}Q;


Q *createQueue(int);
void enQueue(struct Queue *q)
