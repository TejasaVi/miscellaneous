#include "queue.h"

int main(int argc, char *argv[])
{

	Q q;
	if (argc == 2){
		if (intialize(&q, atoi(argv[1]))< 0) {
			printf("Intialization of Queue Failed\n");
			return -1;
		}
	}
	else{
		printf("Intialization of Queue Failed\n");
		return -1;
	}
	enqueue(&q, 10);
	enqueue(&q, 20);
	enqueue(&q, 30);
	enqueue(&q, 40);
	printf("Element at the front = [%d]\n",peek(&q));
	print_queue(&q);
	printf("Removed element : [%d]\n",dequeue(&q));
	print_queue(&q);
	printf("Removed element : [%d]\n",dequeue(&q));
	print_queue(&q);
	printf("Removed element : [%d]\n",dequeue(&q));
	print_queue(&q);
	printf("Removed element : [%d]\n",dequeue(&q));
	print_queue(&q);
	return 0;
}
