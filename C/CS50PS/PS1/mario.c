#include <stdio.h>

int main(void)
{
    int height, row, column, space;

    printf("Enter height here: ");
    scanf("%d", &height);

    while (height < 1 || height > 8);

    //leftside of pyramid
    for(row = 0; row < height; row++)
    {
        for(space = 0; space < (height - row - 1); space++)
        {
            printf(" ");
        }
        for(column = 0; column <= row; column++)
        {
            printf("#");
        }

        //gap
        printf("  ");

        //rightside of pyramid
        for(column = 0; column <= row; column++)
        {
            printf("#");
        }
        printf("\n");
    }

    return 0;
}