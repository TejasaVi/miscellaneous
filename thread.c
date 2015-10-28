#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<string.h>
#include<unistd.h>

pthread_t tid[2];
int counter ;
pthread_mutex_t mux;

void * doSomething(void *args)
{
    unsigned long iter = 0;
    pthread_mutex_lock(&mux);
    counter+=1;
    printf("\nJob %d Started\n",counter);
    for(iter=0;iter< 0xFFFFFFFF;iter++);
    printf("\nJob %d Ended\n",counter);
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
