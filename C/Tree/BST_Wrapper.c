#include "binTree.h"


node* insert(node*R, int data)
{
    if(R == NULL)
       return get_Newnode(data);

    if(R->data < data){
        R->rgt = insert(R->rgt, data);
    }
    else{
        R->lft = insert(R->lft, data);
    }
    return R;
}


int MaxValue(node* R)
{
    return R->data;
}

int Minvalue(node* R)
{
    node* current = R;
    while(current->lft !=NULL)
        current = current->lft;
    return current->data;
}

int ceil(R, int key)
{
}

int main()
{
    node* R = NULL;
    R = insert(R,5);
    R = insert(R,2);
    R = insert(R,3);
    R = insert(R,4);
    R = insert(R,1);
    printTreeInorder(R);printf("\n");
    return 0;
}


