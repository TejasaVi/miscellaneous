/*
        Implementation for consumer.c
*/





#include "common.h"
#include<stdlib.h>
#include <signal.h>

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
    char *char_ret;
    /* Check the passed command line argument */
    if(argc < 3)
    {
        printf("Error: Incorrect number of arguments passed\n");
        exit(EXIT_FAILURE);
    }

    /* initialize max_buffer */
    max_buffer = atoi(argv[1]);

    if (max_buffer <1)
    {
        printf("Error: Atleast 1 shared buffer required\n");
        exit(EXIT_FAILURE);
    }


    /* initialize search_key */
    int i, v = 0, size = argc - 1;
    char *search_key = (char *)malloc(v);

    for(i = 2; i <= size; i++) {
        search_key = (char *)realloc(search_key, (v + strlen(argv[i])));
        strcat(search_key, argv[i]);
        strcat(search_key, " ");
    }
    *(search_key+ strlen(search_key)-1) = '\0';
    printf("Search Key:%s [%d]\n", search_key,strlen(search_key));

    /* POSIX4 style signal handlers */
    struct sigaction sa;
    sa.sa_handler = cleanup;
    sa.sa_flags = 0;
    sigemptyset( &sa.sa_mask );
    (void) sigaction(SIGINT, &sa, NULL);
    (void) sigaction(SIGBUS, &sa, NULL);
    (void) sigaction(SIGSEGV, &sa, NULL);

    //  mutual exclusion semaphore, mutex_sem with an initial value 0.
    if ((mutex_sem = sem_open (SEM_MUTEX_NAME, O_CREAT, 0660, 0)) == SEM_FAILED)
        error ("sem_open:SEM_MUTEX_NAME");

    // Get shared memory
    if ((fd_shm = shm_open (SHARED_MEM_NAME, O_RDWR | O_CREAT, 0660)) == -1)
        error ("shm_open: SHARED_MEM_NAME");

    if (ftruncate (fd_shm, sizeof (struct shared_memory)) == -1)
       error ("ftruncate");

    if ((shared_mem_ptr = mmap (NULL, sizeof (struct shared_memory), PROT_READ | PROT_WRITE, MAP_SHARED,
            fd_shm, 0)) == MAP_FAILED)
       error ("mmap");
    // Initialize the shared memory
    shared_mem_ptr -> buffer_index = shared_mem_ptr -> buffer_print_index = 0;
    // counting semaphore, indicating the number of available buffers. Initial value = MAX_BUFFERS
    if ((buffer_count_sem = sem_open (SEM_BUFFER_COUNT_NAME, O_CREAT, 0660, MAX_BUFFERS)) == SEM_FAILED)
        error ("sem_open");

    // counting semaphore, indicating the number of strings to be printed. Initial value = 0
    if ((spool_signal_sem = sem_open (SEM_SPOOL_SIGNAL_NAME, O_CREAT, 0660, 0)) == SEM_FAILED)
        error ("sem_open");

    // Initialization complete; now we can set mutex semaphore as 1 to
    // indicate shared memory segment is available
    if (sem_post (mutex_sem) == -1)
        error ("sem_post: mutex_sem");
    while (1) {  // forever
        // Is there a string to print? P (spool_signal_sem);
        if (sem_wait (spool_signal_sem) == -1)
            error ("sem_wait: spool_signal_sem");

        // check checksum
        FILE *fp;
        size_t len;
        char buf[4096];

        if (NULL == (fp = fopen(SHARED_MEM_NAME_LOCATION, "rb")))
        {
            printf("Unable to open %s for reading\n", SHARED_MEM_NAME_LOCATION);
            return -1;
        }
        len = fread(buf, sizeof(char), sizeof(buf), fp);
        //printf("In memory: %#x\n",shared_mem_ptr ->checksum);
        //printf("Calculated: %#x\n",shared_mem_ptr ->checksum);
        if(shared_mem_ptr ->checksum != checksum(buf, len, 0)){
            printf("Data Tampered\n");
            continue;
        }
        strcpy (mybuf, shared_mem_ptr -> buf [shared_mem_ptr -> buffer_print_index]);

        /* CHeck for serach key in sentence*/
        char_ret =NULL;
        //    printf("Read Line before: %s", mybuf);
        char_ret = StrStr(mybuf,search_key );
        if (char_ret != NULL){
            // write the string to stdout
            printf("Read Line after: %s", mybuf);
        }
        /* Since there is only one process (the logger) using the
           buffer_print_index, mutex semaphore is not necessary */
        (shared_mem_ptr -> buffer_print_index)++;
        if (shared_mem_ptr -> buffer_print_index == MAX_BUFFERS)
           shared_mem_ptr -> buffer_print_index = 0;

        /* Contents of one buffer has been printed.
           One more buffer is available for use by producers.
           Release buffer: V (buffer_count_sem);  */
        if (sem_post (buffer_count_sem) == -1)
            error ("sem_post: buffer_count_sem");

    }
}
