#include "bin_tree.h"

node* getParentfor(node* root, int data){
    node* tmp;
    if(root == NULL)
        return NULL;
    tmp = root;
    if((tmp->lft->data == data) || (tmp->rgt->data == data))
        return tmp;
    else{
        if(tmp->data > data){
            tmp = tmp->lft;
            tmp = getParentfor(tmp, data);
        }
        else{
            tmp = tmp->rgt;
            tmp = getParentfor(tmp, data);
        }
    }
	return NULL;
}
/*
node* getSiblingfor()
{

}

int getNodeData(node* current)
{
}
*/

void insertLeftChild(node* parent, int data)
{
    node* temp;
    temp = get_Newnode(data);
    parent->lft = temp;
}


void deleteLeftChild(node*parent)
{
    free(parent->lft);
    parent->lft =NULL;
}


void deleteRightChild(node*parent)
{
    free(parent->rgt);
    parent->rgt =NULL;
}


void truncateNode(node*parent)
{
    free(parent->lft);
    parent->lft =NULL;
    free(parent->rgt);
    parent->rgt =NULL;
}


void insertRightChild(node*parent, int data)
{
    node* temp;
    temp = get_Newnode(data);
    parent->rgt = temp;
}


void printTreePreorder(node* root)
{
    if (root != NULL)
    {
        printf("<%d> ", root->data);
        printTreePreorder(root->lft);
        printTreePreorder(root->rgt);
    }
}


void printTreeInorder(node* root)
{
    if (root != NULL)
    {
        printTreeInorder(root->lft);
        printf("<%d> ", root->data);
        printTreeInorder(root->rgt);
    }
}


void printTreePostorder(node* root)
{
    if (root != NULL)
    {
        printTreePostorder(root->lft);
        printTreePostorder(root->rgt);
        printf("<%d> ", root->data);
    }
}


node* get_Newnode(int data)
{
    node* new_ptr = (node*) malloc(sizeof(node));
    new_ptr->data = data;
    new_ptr->lft = NULL;
    new_ptr->rgt = NULL;
    return new_ptr;
}


node* get_EmptyNode()
{
    node* new_ptr = (node*) malloc(sizeof(node));
    return new_ptr;
}


void initBinaryTree(node*Root)
{
    Root->data = 0;
    Root->lft = NULL;
    Root->rgt = NULL;
}
