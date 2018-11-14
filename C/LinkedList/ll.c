#include<stdio.h>
#include<malloc.h>
#include "ll.h"


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

node * insertSorted(node* head, int data){
	node *tmp, *new;
	new = malloc(sizeof(node));
    new->data = data;
    new->nxt = NULL;

	if(head == NULL){
		return new;
	}
	else {
		tmp = head;
		while(tmp->data < data){
			tmp = tmp->nxt;
		}
		new->nxt = tmp->nxt;
		tmp->nxt = new;
	}
	return head;
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


node* insertafterNth(node* head, int n, int data){
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
	return head;
}


void printList(node *head)
{
    node * tmp= head;
    int i=0;
    while(tmp != NULL){
        printf("<%d>", tmp->data);
        tmp = tmp->nxt;i++;
    }
    printf("\n%d nodes present", i);
}

