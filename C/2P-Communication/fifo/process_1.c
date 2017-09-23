/*
*  Process_1 sends a "Hi" message to the Process_2.
*  The communication can be using -
*  1. Shared Memory
*  2. UNIX Sockets
*  3. Named PIPE
*  4. FIFOs
*
*  This program uses, FIFO as communication method
*/


#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>


#define FIFO_NAME "/tmp/example"

int main()
{
    int fd;
    char sender_buf[80] = "Heartbeat:A";
    char receiver_buf[80];

    mkfifo(FIFO_NAME, 0666);
    while (1)
    {
        // Open FIFO for write only
        fd = open(FIFO_NAME, O_WRONLY);
        write(fd, sender_buf, strlen(sender_buf)+1);
        close(fd);

        // Open FIFO for Read only
        fd = open(FIFO_NAME, O_RDONLY);

        // Read from FIFO
        read(fd, receiver_buf, sizeof(receiver_buf));

        // Print the read message
        printf("Process 2: %s\n", receiver_buf);
        close(fd);
    }
    close(fd);
    return 0;
}

