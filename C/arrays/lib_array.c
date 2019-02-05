#include<stdio.h>

int sum_of_all_elements(int array[], int len) {
	int i = 0;
	int sum=0;
	for(i = 0;i<len;i++)
		sum += array[i];
	return sum;
}


void print_array(int arr[], int len) {
	printf("\n");
	for(int i=0;i<len;i++) {
		printf("%d ",arr[i]);
	}
	printf("\n");
}

void move_all_zeros_at_end(int arr[], int len) {
	print_array(arr,len);
	int count =0;
	for(int i=0;i<len;i++) {
		if (arr[i] != 0) {
			arr[count++] = arr[i];
		}
	}
	while(count<len) {
		arr[count++] = 0;
	}
	print_array(arr,len);
	return ;
}


void print_alternate_element(int *param, int size) {
    for(int i=0; i<size; i= i+2) {
        printf("%d ",*(param+i));
    }
    printf("\n");
}
void LeftShiftByOne(int array[], int len) {
	int temp, i;
	temp = array[0];
	for(i=0; i<len-1; i++) {
		array[i] = array[i+1];
	}
	array[i] = temp;
}

void RightShiftByOne(int array[], int len) {
	int temp, i;
	temp = array[len-1];

	for(i=len-1; i>0; i--) {
		array[i] = array[i-1];
	}
	array[0] = temp;
}

void printArray(int arr[], int len){
	int i;
	printf("[");
	for(i=0;i<len;i++)
		printf("%d ",arr[i]);
	printf("]\n");

}

void rotate_array(int array[], int len, int RotateBy, int right_shift) {
	int i;
	RotateBy = RotateBy%len;

	if (right_shift){
			printf("Rotating Right by %d hop\n", RotateBy);
			for(i=0; i<RotateBy;i++) {
				RightShiftByOne(array, len);
			}
	} else {
			printf("Rotating Left by %d hop\n", RotateBy);
			for(i=0; i<RotateBy;i++) {
				LeftShiftByOne(array, len);
			}

	}
}


