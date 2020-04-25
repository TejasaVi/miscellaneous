#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<string.h>
#include <sys/types.h>
#include<unistd.h>

pthread_t tid[2];
pthread_mutex_t mux;

void * doSomething(void *args)
{
    pthread_mutex_lock(&mux);
	printf("_________________________\n");
	printf("From the function, the thread id = %d\n", pthread_self());
	printf("PID : %jd\n",getpid());
	printf("PPID : %jd\n",getppid());
	printf("_________________________\n");
    pthread_mutex_unlock(&mux);
    return NULL;

}

int main()
{
    int i =0;
    int err;

    if(pthread_mutex_init(&mux, NULL) !=0)
    {
        printf("\nmutex init failed\n");
        return 1;
    }
    while(i<2)
    {
        err = pthread_create(&tid[i],NULL,&doSomething,NULL);
        if(err !=0)
            printf("\nFailed to create thread [%s]\n",strerror(err));
        i++;
    }
    pthread_join(tid[0],NULL);
    pthread_join(tid[1],NULL);
    pthread_mutex_destroy(&mux);
    return 0;
}
