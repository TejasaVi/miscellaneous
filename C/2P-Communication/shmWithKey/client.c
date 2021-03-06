#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>


int main(int argc, char *argv[])
{
    key_t key;
    int shmid;
    char *data;
    int mode;
	FILE *fp;
	int max_buffer = 0;
    if (argc > 3) {
        fprintf(stderr, "usage: server [substring] [buffer_size]\n");
        exit(1);
    }
    max_buffer = atoi(argv[2]);
    if (max_buffer <1)
    {
        perror("Error: Atleast 1 shared buffer required\n");
        exit(EXIT_FAILURE);
    }
    max_buffer = max_buffer*1024;

    /* make the key: */
    if ((key = ftok("server.c", 'R')) == -1) {
        perror("ftok");
        exit(1);
    }


    /* connect to (and possibly create) the segment: */
    if ((shmid = shmget(key, max_buffer, 0644 | IPC_CREAT)) == -1) {
        perror("shmget");
        exit(1);
    }

    /* attach to the segment to get a pointer to it: */
    data = shmat(shmid, (void *)0, 0);
    if (data == (char *)(-1)) {
        perror("shmat");
        exit(1);
    }

    /* read or modify the segment, based on the command line: */
	printf("segment contains: \"%s\"\n", data);

    /* detach from the segment: */
    if (shmdt(data) == -1) {
        perror("shmdt");
        exit(1);
    }

    return 0;
}
