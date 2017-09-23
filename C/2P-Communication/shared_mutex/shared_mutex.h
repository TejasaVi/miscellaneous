#ifndef SHARED_MUTEX_H
#define SHARED_MUTEX_H

#define _BSD_SOURCE // for ftruncate
#include <pthread.h> // pthread_mutex_t, pthread_mutexattr_t,
                     // pthread_mutexattr_init, pthread_mutexattr_setpshared,
                     // pthread_mutex_init, pthread_mutex_destroy

// Structure of a shared mutex.
typedef struct shared_mutex_t {
  pthread_mutex_t *ptr; // Pointer to the pthread mutex and
                        // shared memory segment.
  int shm_fd;           // Descriptor of shared memory object.
  char* name;           // Name of the mutex and associated
                        // shared memory object.
  int created;          // Equals 1 (true) if initialization
                        // of this structure caused creation
                        // of a new shared mutex.
                        // Equals 0 (false) if this mutex was
                        // just retrieved from shared memory.
} shared_mutex_t;

shared_mutex_t shared_mutex_init(char *name);

int shared_mutex_close(shared_mutex_t mutex);

int shared_mutex_destroy(shared_mutex_t mutex);

#endif // SHARED_MUTEX_H
