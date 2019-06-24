#include<stdio.h>
#include <stdlib.h>

typedef struct semaphore_t {
	int value;
	int cntr;
}semaphore_t;

semaphore_t *init(semaphore_t *, int value);
semaphore_t *wait(semaphore_t *);
semaphore_t *signal(semaphore_t *);
void destroy(semaphore_t *);

void destroy(semaphore_t *sem){
	free(sem);
}

semaphore_t *signal(semaphore_t *sem){
	printf("Semaphore value before signal:[%d]\n",sem->cntr);
	while(sem->cntr == sem->value);
	sem->cntr = sem->cntr + 1;
	printf("Semaphore value after signal:[%d]\n",sem->cntr);
	return sem;
}

semaphore_t *wait(semaphore_t *sem){
	printf("Semaphore value before wait:[%d]\n",sem->cntr);
	while(sem->cntr <= 0);
	sem->cntr = sem->cntr -1;
	printf("Semaphore value after wait:[%d]\n",sem->cntr);
	return sem;
}

semaphore_t *init(semaphore_t *sem, int value){
	sem = malloc(sizeof(semaphore_t));
	sem->value = value;
	sem->cntr = 0;
	return sem;
}


int main(){
	semaphore_t *sem;
	sem = init(sem, 5);
	sem = signal(sem);
	sem = wait(sem);
	destroy(sem);
}
