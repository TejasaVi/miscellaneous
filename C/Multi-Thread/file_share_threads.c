#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<string.h>
#include<unistd.h>
#define LOCATION "./file"
pthread_t treader[2],twriter[2];
FILE* fptr;
pthread_mutex_t mux;

void * doRead(void *args)
{
    unsigned long iter = 0;
	char buffer[100];
    pthread_mutex_lock(&mux);
	if(!feof(fptr)){
		fread(buffer, sizeof(buffer), 8, fptr);
		printf("%s",buffer);
	}
    pthread_mutex_unlock(&mux);
    return NULL;

}

void * doWrite(void *args){
	unsigned long iter = 0;
	char buffer[] = "blahblah";
	pthread_mutex_lock(&mux);
		fread(buffer,sizeof(buffer), 8,fptr);
	pthread_mutex_unlock(&mux);
}

int main()
{
    int i =0;
    int err;
	fptr = fopen(LOCATION, "a+");
    if(fptr == NULL){
		printf("\nFile open failed.\n");
		return 1;
	}

    if(pthread_mutex_init(&mux, NULL) !=0)
    {
        printf("\nmutex init failed\n");
        return 1;
    }
    while(i<2)
    {
        err = pthread_create(&twriter[i],NULL,&doWrite,NULL);
        if(err !=0)
            printf("\nFailed to create thread [%s]\n",strerror(err));
        err = pthread_create(&treader[i],NULL,&doRead,NULL);
        if(err !=0)
            printf("\nFailed to create thread [%s]\n",strerror(err));
        i++;
    }

	for(i=0;i<2;i++){
    	pthread_join(treader[i],NULL);
    	pthread_join(twriter[i],NULL);
	}
    pthread_mutex_destroy(&mux);
	fclose(fptr);
    return 0;
}
