typedef struct {
struct node * nxt;
int data;
}node;




node* insert(node* , int );
node* insertSorted(node*, int);
node* addBeforeHead(node *, int);
node* insertafterNth(node*, int, int );
void printList(node *);

