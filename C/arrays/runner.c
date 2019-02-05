#include <stdio.h>
#include "lib_array.h"


int main(int argc, char *argv[]) {
	int i;
	int num_of_elements = 0;
	printf("Enter number of elements in array:");
	scanf("%d",&num_of_elements);
	int array[num_of_elements];
	printf("Enter elements in array:");
	for(i; i<num_of_elements; i++) {
		scanf("%d",&array[i]);
	}
	int op;
	scanf("%d",&op);
	/* switch to functions */
	switch(op) {

	case 5:
			printf("Enter the Rotation hops:");
			scanf("%d",&i);
			rotate_array(array,num_of_elements,i, 0);
			print_array(array,num_of_elements);
			break;
	case 4:
			rotate_array(array,num_of_elements,4, 1);
			print_array(array,num_of_elements);
			break;
	case 3:
			printf("Alternate elements of array are:");
			print_alternate_element(array, num_of_elements);
			break;
	case 2:
			printf("Array after moving zeros at the end:");
			move_all_zeros_at_end(array, num_of_elements);
			break;
	case 1:
			printf("Sum of all elements of an array is :%d\n ",sum_of_all_elements(array, num_of_elements));
			break;
	default:
			printf("Operation not defined");
	}
	return 0;
}
