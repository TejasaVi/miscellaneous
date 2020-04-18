#include "bin_tree.h"


int GetSumForPath(node *root,int node_data){
	int sum = 0,subsum = 0;

	if(root->data == node_data){
		return node_data;
	}
	else if ((node_data < root->data )&& (root->lft != NULL)){
		subsum = GetSumForPath(root->lft, node_data);
		if( subsum != 0)
			sum = root->data + subsum;
		else
			sum = 0;
		return sum;
	}
	else if((node_data > root->data) && (root->rgt != NULL)){
		subsum = GetSumForPath(root->rgt, node_data);
		if( subsum != 0)
			sum = root->data + subsum;
		else
			sum = 0;
		return sum;
	}
	else if((root->data != node_data )&& (root->lft == NULL) && (root->rgt == NULL)){
		return 0;
	}
return 0;
}


int GetNumNodes(node* root){
	if(root ==NULL){
		return 0;
	}
	return (1+ GetNumNodes(root->lft) + GetNumNodes(root->rgt));
}


void DeleteTree(node*root){
	if(root == NULL)
		return;
	DeleteTree(root->lft);
	DeleteTree(root->rgt);
	free(root);
}


int getSumofTree(node*root)
{
	node* tmp=NULL;
	int sum = 0;
	if(root == NULL)
		goto end;
	tmp = root;
	sum = tmp->data;
	printf("[%d]->\n",tmp->data);
	while(tmp !=NULL){
		sum += getSumofTree(tmp->lft);
		sum += getSumofTree(tmp->rgt);
	}
end:
	return sum;
}

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


node* getSiblingfor(node*root,int data)
{
	node *tmp, *parent;
	if(root ==NULL)
		return NULL;
	tmp = root;
	parent = getParentfor(tmp,data);
	if(parent->lft->data ==data)
		return parent->rgt;
	return parent->lft;
}

int getNodeData(node* current)
{
	if(!current){
		return current->data;
	}
	return -1;
}

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
