#include <stdio.h>
#include "shared_mutex.h"


int main(){
	shared_mutex_t mutex = shared_mutex_init("/my-mutex");
	if (mutex.ptr == NULL) {
			return -1;
	}

	if(mutex.created) {
		printf("Mutex created\n");
	}

	// critical region
	pthread_mutex_lock(mutex.ptr);
	printf("Press key to unlock\n");
	getchar();
	pthread_mutex_unlock(mutex.ptr);
	
	if(shared_mutex_close(mutex)) {
		return 1;
	}
	return 0;
}
