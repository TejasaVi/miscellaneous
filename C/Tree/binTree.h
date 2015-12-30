#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

typedef struct{
    int data;
    struct node* lft;
    struct node* rgt;
}node;


node* get_Newnode(int );
node* get_EmptyNode();
void insertLeftChild(node* , int );
void insertRightChild(node* , int );
void deleteLeftChild(node*);
void deleteRightChild(node*);
void truncateNode(node*);
void printTreePreorder(node* );
void printTreePostorder(node* );
void printTreeInorder(node* );
void initBinaryTree(node*);
