#include <stdio.h>
/*
* 1. Array declration.
* 2. passing arrays to function.
* 3. pointer to arrays.
*
*/
void print_array_as_pointer(int *param, int size) {
	for(int i=0; i<size; i++) {
		printf("%d ",*(param+i));
	}
	printf("\n");
}

void print_array_as_unsized_array(int param[], int size) {
	for(int i=0; i<size; i++) {
		printf("%d ",param[i]);
	}
	printf("\n");
}



int main() {
	// 1. Array declration.
	int arr_1[10];

	int arr_2[] = {1,2,3,4,5,6};
	print_array_as_pointer(arr_2, sizeof(arr_2)/sizeof(int));
	print_array_as_unsized_array(arr_2, sizeof(arr_2)/sizeof(int));
	return 0;
}
