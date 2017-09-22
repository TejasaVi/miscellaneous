#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <semaphore.h>
#include <sys/mman.h>


// Buffer data structures
#define MAX_BUFFERS 10


#define SEM_MUTEX_NAME "/sem-mutex"
#define SEM_BUFFER_COUNT_NAME "/sem-buffer-count"
#define SEM_SPOOL_SIGNAL_NAME "/sem-spool-signal"
#define SHARED_MEM_NAME "/untrusted-shared-mem"
#define SHARED_MEM_NAME_LOCATION "/dev/shm/untrusted-shared-mem"
struct shared_memory {
    char buf [MAX_BUFFERS] [1024];
    unsigned  checksum;
    int buffer_index;
    int buffer_print_index;
};


// Max number of Buffers allowed.
int max_buffer = 0;


// Function declarations
void error (char *msg);
unsigned checksum(void *buffer, size_t len, unsigned int seed);
char* StrStr(char *str, char *substr);
void cleanup(int calledViaSignal);
