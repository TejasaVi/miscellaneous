#include "bit_ops.h"
/*
Compute integer absolute value without branching
*/
int abs(int number)
{
    int const mask = number >> sizeof(int)* CHAR_BIT -1;
    return (number^mask) - mask;
}


/*
Swap two numbers without temporary variable.
*/
void swap(int* first, int* second)
{
    *first = *first^*second;
    *second= *first^*second;
    *first = *first^*second;
    return;
}

/*
Find minimum value from two integers.Without if-else.
*/
int findMinimumof(int first, int second){
    return second^((first^second)&-(first<second));
}

/*
Find maximum value from two integers.Without if-else.
*/
int findMaximumof(int first, int second){
    return second^((first^second)&-(first>second));
}

/*
Masking the Least significant 1bit from a number.
*/
int maskLS1(int number)
{
    return (number & ( -number ));
}

/*
Set a bit in flag at given position.
*/
int set_flagbit(int flag, int bitnum)
{
    return flag |= 1 << bitnum;
}


/*
Clear a bit in flag at given position.
*/
int clear_flagbit(int flag, int bitnum)
{
    return flag &= ~(1 << bitnum);
}


/*
Toggle a bit in flag at given position.
*/
int toggle_flagbit(int flag, int bitnum)
{
    return flag ^= 1 << bitnum;
}

/*
Check if the given position bit is set.
*/
int check_bitset(int flag, int bitnum)
{
    return (flag>>bitnum)& 1;
}

