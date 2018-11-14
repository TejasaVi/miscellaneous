#include "ll.h"
#include<stdio.h>


int main(){
	node * Head;
    int i,data;
    Head = NULL;
    for(i=0; i<6;i++){
       scanf("%d",&data);
       Head = insertSorted(Head, data);
    }
    printList(Head);
    /*
	for(i=0; i<6;i++){
       scanf("%d",&data);
        Head = addBeforeHead(Head, data);
    }
    printList(Head);
    scanf("%d",&data);
    Head = insertafterNth(Head,5,data);
    printList(Head);
	*/
    return 0;

}
