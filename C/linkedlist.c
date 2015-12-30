#include<stdio.h>
#include<malloc.h>

typedef struct {
struct node * nxt;
int data;
}node;


node * insert(node *head, int data)
{
    node *tmp, *new;
    new = malloc(sizeof(node));
    new->data = data;
    new->nxt = NULL;

    if(head == NULL){
        return new;
    }
    else{
        tmp = head;
        while(tmp->nxt != NULL)
            tmp = tmp->nxt;
        tmp->nxt = new;
    }

    return head;
}

void print(node *head)
{
    node * tmp= head;
    int i=0;
    while(tmp != NULL){
        printf("<%d>", tmp->data);
        tmp = tmp->nxt;i++;
    }
    printf("\n%d nodes present", i);
}


node * addBeforeHead(node *head, int data){
    node *tmp, *new;
    new = malloc(sizeof(node));
    new->data = data;
    new->nxt = NULL;
    tmp = head;
    if(tmp == NULL){
        return new;
    }
    else{
        head = new;
        new->nxt = tmp;
    }
    return head;
}

void insertafterNth(node* head, int n, int data){
    node *tmp, *new;
    int i;
    new = malloc(sizeof(node));
    new->data = data;
    new->nxt = NULL;
    tmp = head;
    printf("\n%d %d \n", data, n);
    for(i=0; i<n; i++){
        tmp = tmp->nxt;
    }
    new->nxt = tmp->nxt;
    tmp->nxt = new;

}
int main ()
{
    node * Head;
    int i,data;
    Head = NULL;
    for(i=0; i<6;i++){
       scanf("%d",&data);
        Head = insert(Head, data);
    }
    print(Head);
    for(i=0; i<6;i++){
       scanf("%d",&data);
        Head = addBeforeHead(Head, data);
    }
    print(Head);
    scanf("%d",&data);
    insertafterNth(Head,5,data);
    print(Head);
    return 0;
}
