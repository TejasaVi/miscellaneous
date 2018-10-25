
static int count;

typedef struct Node{
    int bufferID;
    struct Node *next;
}node;


typedef struct Queue{
	int size;
	node *front, *end;
}Q;


Q* createQ(int);
void enQueue(struct Queue *q, int k);
node* deQueue(struct Queue *q);
