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
    char sender_buf[80];
    char receiver_buf[80] = "Heartbeat:B";
    // FIFO file path
    mkfifo(FIFO_NAME, 0666);

    while (1)
    {
        // First open in read only and read
        fd = open(FIFO_NAME,O_RDONLY);
        read(fd, receiver_buf, 80);

        // Print the read string and close
        printf("Process 1: %s\n", receiver_buf);
        close(fd);

        // Now open in write mode and write
        // string taken from user.
        fd = open(FIFO_NAME,O_WRONLY);
        write(fd, sender_buf, strlen(sender_buf)+1);
        close(fd);
    }
    return 0;
}
