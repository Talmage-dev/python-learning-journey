#include <stdio.h>

int main(void)
{
    // Prompt for start size
    int start;
    do
    {
        printf("What is the Starting population? (must be greater than 9): ");
        scanf("%d", &start);
    } while (start < 9);
    
    // Prompt for end size
    int end;
    do
    {
        printf("What is the Ending Population? (must be greater than starting population); ");
        scanf("%d", &end);
    } while (start > end);
    
    //Calculate number of years until we reach threshold
    int years = 0;
    do
    {
        start = start + (start/3) - (start/4);
        years++;
    } while (start < end);

    // Print number of years
    printf("Years: %i\n", years);

    return 0;
}