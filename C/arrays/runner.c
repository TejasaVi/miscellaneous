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
	printf("Choose Array Operation:\n1)Sum of all items\n2)Move zeros at end\n3)Print Alternate items\n4)Rotate Right\n5)Rotate Left\n6)Bubble Sort\n7)Selection Sort \n8)\n9) \n10)\n");
	scanf("%d",&op);
	/* switch to functions */
	switch(op) {
	case 7:
			selection_sort(array, num_of_elements);
			printf("Array after Selection Sorting:");
			print_array(array,num_of_elements);
			break;

	case 6:
			bubble_sort(array, num_of_elements);
			printf("Array after Bubble Sorting:");
			print_array(array,num_of_elements);
			break;
	case 5:
			printf("Enter the Rotation hops:");
			scanf("%d",&i);
			rotate_array(array,num_of_elements,i, 0);
			print_array(array,num_of_elements);
			break;
	case 4:
			printf("Enter the Rotation hops:");
			scanf("%d",&i);
			rotate_array(array,num_of_elements, i, 1);
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
