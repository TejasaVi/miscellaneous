#include<stdio.h>
#include<stdlib.h>
typedef struct mutex_t {
	int lock;
}mutex_t;

mutex_t *init();
void destory(mutex_t *);
mutex_t *lock(mutex_t*);
mutex_t *unlock(mutex_t*);

mutex_t *unlock(mutex_t*mutex){
	if(mutex->lock){
		mutex->lock = 0;
		printf("Mutex Unlocked\n");
	}
	return mutex;
}

mutex_t *lock(mutex_t*mutex){
    if(!mutex->lock){
        mutex->lock = 1;
		printf("Mutex Locked\n");
    }
    return mutex;
}

mutex_t *init(){
	mutex_t *mutex = malloc(sizeof(mutex_t));
	mutex->lock = 0;
	return mutex;
}

void destory(mutex_t *mutex){
	free(mutex);
}


int main(){
	mutex_t *mutex;
	mutex = init();
	mutex = lock(mutex);
	mutex = unlock(mutex);
	destory(mutex);
	return 0;
}
