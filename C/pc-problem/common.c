#include <string.h>
#include <stdlib.h>
#include<stdio.h>

// Print system error and exit
void error (char *msg)
{
    perror (msg);
    exit (1);
}

//Calculate checksum of content
unsigned checksum(void *buffer, size_t len, unsigned int seed)
{
      unsigned char *buf = (unsigned char *)buffer;
      size_t i;

      for (i = 0; i < len; ++i)
            seed += (unsigned int)(*buf++);
      return seed;
}

// Finds the substring
char* StrStr(char *str, char *substr)
{
      while (*str)
      {
            char *Begin = str;
            char *pattern = substr;
            // If first character of sub string match, check for whole string
            while (*str && *pattern && *str == *pattern)
            {
                  str++;
                  pattern++;
            }
            // If complete sub string match, return starting address
            if (!*pattern)
                  return Begin;
            str = Begin + 1;    // Increament main string
      }
      return NULL;
}

