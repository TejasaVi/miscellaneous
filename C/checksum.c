/*
**  CHECKSUM.C - Compute the checksum of a file
**
**  public somain demo by Bob Stout
*/

#include <stdlib.h>
#include <stdio.h>

unsigned checksum(void *buffer, size_t len, unsigned int seed)
{
    // The seed cna be changed with a approiate algo to get better  secure
    //checksum
    unsigned char *buf = (unsigned char *)buffer;
    size_t i;

    for (i = 0; i < len; ++i)
        seed += (unsigned int)(*buf++);
    return seed;
}



int main(int argc, char *argv[] )
{
    FILE *fp;
    size_t len;
    if (argc!=2){
        printf("Less args\n");
        exit(1);
    }
    char buf[4096], *file = argv[1];
    printf("File : %s\n",file);
    if (NULL == (fp = fopen(file, "rb")))
    {
        printf("Unable to open %s for reading\n", file);
        return -1;
    }
    len = fread(buf, sizeof(char), sizeof(buf), fp);
    printf("%d bytes read\n", len);
    printf("The checksum of %s is %#x\n", file, checksum(buf, len, 0));
    return 0;
}

