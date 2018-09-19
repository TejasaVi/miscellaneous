#include "bin_tree.h"

int main ()
{
    node* R, *tmp;
    R = get_EmptyNode();
    initBinaryTree(R);
    R = get_Newnode(5);
    insertLeftChild(R,1);
    insertRightChild(R,2);
    printTreeInorder(R);printf("\n");
	tmp = getParentfor(R,2);
	printf("Parent for <%d> is <%d>\n",2, tmp->data);
    return 0;
}

