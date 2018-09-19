#include <stdio.h>
/*
* 1. Array declration.
* 2. passing arrays to function.
* 3. pointer to arrays.
*
*/
void print_alternate_element(int *param, int size) {
	for(int i=0; i<size; i= i+2) {
		printf("%d ",*(param+i));
	}
	printf("\n");
}

int main() {
	// 1. Array declration.
	int arr_1[10];

	int arr_2[] = {1,2,3,4,5,6};
	for(int i=0;i<sizeof(arr_2)/sizeof(int);i++)
		printf("%d ",arr_2[i]);
	printf("\n");
	print_alternate_element(arr_2, sizeof(arr_2)/sizeof(int));
	return 0;
}
