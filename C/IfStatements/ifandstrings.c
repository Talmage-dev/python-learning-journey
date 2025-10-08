#include <stdio.h>
#include <string.h>

int main()
{
    char name[50] = ""; // Initialize name with an empty string

    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = 0; // Remove the newline character if present

    if(strlen(name) == 0)
    {
        printf("You didn't enter a name.\n");
    }
    else if (strcmp(name, "Alice") == 0)
    {
        printf("Hello, Alice! Welcome back!\n");
    }
    else if (strcmp(name, "Bob") == 0)
    {
        printf("Hello Bob! Good to see you again!\n");
    }
    else
    {
        printf("Hello, %s! Nice to meet you!\n", name);
    }
}