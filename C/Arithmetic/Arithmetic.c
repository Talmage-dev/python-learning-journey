#include <stdio.h>

int main()
{
    // Arithmatic operations = + - * / % ++ --
    int x = 10;
    int y = 2;
    int z = 0;

    z = x + y; // Addition
    printf("x + y = %d\n", z);

    z = x - y; // Subtraction
    printf("x - y = %d\n", z);

    z = x * y; // Multiplication
    printf("x * y = %d\n", z);
    
    z = x / y; // Division
    printf("x / y = %d\n", z);

    z = y % x; // Modulous
    printf("x %% y = %d\n", z);

    x++; // Increment by 1
    printf("x++ = %d\n", x);

    y--; //Decrement
    printf("y-- = %d\n", y);

    // Shorthand arthimethic operations
    // Add by 2 to x
    x += 2; // x = x + 2
    printf("x += 2 -> x = %d\n", x);

    // Subtract 2 from x
    x -= 2; // x = x - 2
    printf("x -= 2 -> x = %d\n", x);

    // Multiply x by 2
    x *= 2; // x = x * 2
    printf("x *= 2 -> x = %d\n", x);

    // Divide x by 2
    x /= 2; // x = x / 2
    printf("x /= 2 -> x = %d\n", x);

    return 0;
}