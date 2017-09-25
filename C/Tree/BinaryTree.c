#include "bin_tree.h"

int main ()
{
    node* R;
    R = get_EmptyNode();
    initBinaryTree(R);
    R = get_Newnode(5);
    insertLeftChild(R,1);
    insertRightChild(R,2);
    printTreeInorder(R);printf("\n");
    return 0;
}

