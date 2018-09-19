#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

typedef struct Node node;
typedef struct Node{
    int data;
    struct Node* lft;
    struct Node* rgt;
}node;


node* get_Newnode(int );
node* get_EmptyNode();
node* getParentfor(node*, int);
void insertLeftChild(node* , int );
void insertRightChild(node* , int );
void deleteLeftChild(node*);
void deleteRightChild(node*);
void truncateNode(node*);
void printTreePreorder(node* );
void printTreePostorder(node* );
void printTreeInorder(node* );
void initBinaryTree(node*);
