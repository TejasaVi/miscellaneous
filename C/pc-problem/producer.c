/*
        Implementation for producer.c
 */

#include "common.h"
#include <signal.h>

void error (char *msg);

/* signal handler to clean up in case of premature termination */
void cleanup(int calledViaSignal) {
    shm_unlink(SHARED_MEM_NAME);
    sem_unlink(SEM_MUTEX_NAME);
    sem_unlink(SEM_BUFFER_COUNT_NAME);
    sem_unlink(SEM_SPOOL_SIGNAL_NAME);

    if (calledViaSignal) {
        exit(3);
    }
}



int main (int argc, char **argv)
{
    struct shared_memory *shared_mem_ptr;
    sem_t *mutex_sem, *buffer_count_sem, *spool_signal_sem;
    int fd_shm;
    char mybuf [1024];

    FILE *input_file;
    char tmp[1024];
    /* Check the passed command line argument */
    if(argc != 3)
    {
        error("Error: Incorrect number of arguments passed\n");
        exit(EXIT_FAILURE);
    }

    /* initialize max_buffer */
    max_buffer = atoi(argv[1]);
    if (max_buffer <1)
    {
        error("Error: Atleast 1 shared buffer required\n");
        exit(EXIT_FAILURE);
    }
    /* Open input file */
    if((input_file = fopen(argv[2],"r")) == NULL)
    {
        perror("fopen failed");
        exit(EXIT_FAILURE);
    }

    /* POSIX4 style signal handlers */
    struct sigaction sa;
    sa.sa_handler = cleanup;
    sa.sa_flags = 0;
    sigemptyset( &sa.sa_mask );
    (void) sigaction(SIGINT, &sa, NULL);
    (void) sigaction(SIGBUS, &sa, NULL);
    (void) sigaction(SIGSEGV, &sa, NULL);

    //  mutual exclusion semaphore, mutex_sem
    if ((mutex_sem = sem_open (SEM_MUTEX_NAME, 0, 0, 0)) == SEM_FAILED)
        error ("sem_open: SEM_MUTEX_NAME");

    // Get shared memory
    if ((fd_shm = shm_open (SHARED_MEM_NAME, O_RDWR, 0)) == -1)
        error ("shm_open: SHARED_MEM_NAME");

    if ((shared_mem_ptr = mmap (NULL, sizeof (struct shared_memory), PROT_READ | PROT_WRITE, MAP_SHARED,
            fd_shm, 0)) == MAP_FAILED)
       error ("mmap");

    // counting semaphore, indicating the number of available buffers.
    if ((buffer_count_sem = sem_open (SEM_BUFFER_COUNT_NAME, 0, 0, 0)) == SEM_FAILED)
        error ("sem_open: SEM_BUFFER_COUNT_NAME");

    // counting semaphore, indicating the number of strings to be printed. Initial value = 0
    if ((spool_signal_sem = sem_open (SEM_SPOOL_SIGNAL_NAME, 0, 0, 0)) == SEM_FAILED)
        error ("sem_open: SEM_SPOOL_SIGNAL_NAME");

    char buf [1024];

    while (fgets (buf, 1024, input_file)) {
        // remove newline from string
        int length = strlen (buf);
        if (buf [length - 1] == '\n')
           buf [length - 1] = '\0';

        // get a buffer: P (buffer_count_sem);
        if (sem_wait (buffer_count_sem) == -1)
            error ("sem_wait: buffer_count_sem");

        /* There might be multiple producers. We must ensure that
            only one producer uses buffer_index at a time.  */
        // P (mutex_sem);
        if (sem_wait (mutex_sem) == -1)
            error ("sem_wait: mutex_sem");

        // Critical section
            sprintf (shared_mem_ptr -> buf [shared_mem_ptr -> buffer_index], "%d\n%s\n", strlen(buf),buf);
            (shared_mem_ptr -> buffer_index)++;
            if (shared_mem_ptr -> buffer_index == MAX_BUFFERS)
                shared_mem_ptr -> buffer_index = 0;

        //Print the buffer  writen data on screen
        printf("Writen by Producer:%d\n%s\n", strlen(buf), buf);
        FILE *fp;
        size_t len;
        char buf[4096];

        if (NULL == (fp = fopen(SHARED_MEM_NAME_LOCATION, "rb")))
        {
            printf("Unable to open %s for reading\n", SHARED_MEM_NAME_LOCATION);
            return -1;
        }
        len = fread(buf, sizeof(char), sizeof(buf), fp);
        shared_mem_ptr ->checksum = checksum(buf, len, 0);
        // Release mutex sem: V (mutex_sem)
        if (sem_post (mutex_sem) == -1)
            error ("sem_post: mutex_sem");


    // Tell spooler that there is a string to print: (spool_signal_sem);
        if (sem_post (spool_signal_sem) == -1)
            error ("sem_post: (spool_signal_sem");

    }

    if (munmap (shared_mem_ptr, sizeof (struct shared_memory)) == -1)
        error ("munmap");
    exit (0);
}
