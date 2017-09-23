#include <stdio.h>
#include <stdlib.h>
#include <uuid/uuid.h>

#include <fcntl.h> // O_RDWR, O_CREATE
#include <linux/limits.h> // NAME_MAX
#include <sys/mman.h> // shm_open, shm_unlink, mmap, munmap,
                      // PROT_READ, PROT_WRITE, MAP_SHARED, MAP_FAILED
#include <unistd.h> // ftruncate, close


void error (char *msg) { perror (msg); exit (1); }

void *s_mem_alloc(char name[], int size)
{
	void * shared_mem_ptr;
	int fd_shm;
	if (name == NULL)
		name = "head";

	// open shared memory
	if ((fd_shm = shm_open (name, O_RDWR | O_CREAT, 0660)) == -1)
		error ("shm_open");

	if (ftruncate (fd_shm, size) == -1)
		error ("ftruncate"); 

	if ((shared_mem_ptr = mmap (NULL, size, PROT_READ | PROT_WRITE, MAP_SHARED, fd_shm, 0)) == MAP_FAILED)
		error ("mmap");
	return shared_mem_ptr;
}

void s_mem_free(void * shared_mem_ptr, int size)
{
	if (munmap (shared_mem_ptr, size) == -1)
		error ("munmap");
	printf("SHM destroyed\n");
}

void s_mem_destroy(char name[])
{
	if(shm_unlink(name) == -1)
		error("shm_unlink");
}

int main()
{
	uuid_t uuid;
	uuid_generate_time_safe(uuid);
	char uuid_str[37];
	uuid_unparse_lower(uuid, uuid_str);

	s_mem_alloc(NULL, 1);
	s_mem_alloc(uuid_str, 1);
	return 0;
}
