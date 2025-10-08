#include <stdio.h>
#include <math.h>

int main(void)
{
    float dollar;

    do
    {
    //get a dollar amount
    printf("Enter your change: ");
    scanf("%f", &dollar);
    }
    while(dollar <= 0);

    int cents = round(dollar * 100);
    int coins = 0;

    while(cents >= 200)
    {
        cents -= 200;
        coins++;
    }
    while(cents >= 100)
    {
        cents -= 100;
        coins++;
    }
    while(cents >= 50)
    {
        cents -= 50;
        coins++;
    }
    while(cents >= 20)
    {
        cents -= 20;
        coins++;
    }
    while(cents >= 10)
    {
        cents -= 10;
        coins++;
    }

    //display number of coins
    printf("You will need at least %i coins\n", coins);

    return 0;
}