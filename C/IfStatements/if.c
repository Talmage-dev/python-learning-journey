#include <stdio.h>

int main()
{
    int age;

    printf("Enter your age: ");
    scanf("%d", &age);

    if (age >= 65)
    {
        printf("You are a senior citizen.\n");
    }
    else if (age >= 18)
    {
        printf("You are an adult.\n");
    }
    else if (age < 0)
    {
        printf("You haven't been born yet!\n");
    }
    else if (age == 0)
    {
        printf("You are a newborn!\n");
    }
    else
    {
        printf("You are a child.\n");
    }

    return 0;
}