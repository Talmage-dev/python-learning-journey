#include <stdio.h>
void meow(int n);

int main(void)
{
    meow(6);

    return 0;
}

//meow function
void meow(int n)
{
    for (int i = 0; i < n; i++);
    {
        printf("meow\n");
    }
}