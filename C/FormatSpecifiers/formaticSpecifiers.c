#include <stdio.h>

int main()
{
    /* Format specifier = Special tokens that begin with a % character,
                          followed by  a character that represents the data type
                          and optional modifiersw (width, precision, etc).
                          They control how the data is displayed or interpreted.
                          Used in functions like printf() and scanf(). */

    int age = 25;
    float price = 19.99;
    double pi = 3.14159265389793;
    char currency = '$';
    char name[] = "Talmage";

    printf("Hello, %s!\n", name);               // %s = String
    printf("You are %d years old.\n", age);     // %d = Integer (whole number)
    printf("The price for a Pizza iss %c%.2f.\n", currency, price); // %c = character, %.2f = Float (decimal number) with 2 decimal places
    printf("The value of pi is approximately %.5f.\n", pi); // %.5f = Float with 5 decimal places
    printf("You are %d years old. In 5 years, you will be %d.\n", age, age + 5); // Using multiple format specifiers

    /* Width Examples */

    int num1 = 1;
    int num2 = 10;
    int num3 = 100;
    // Display numbers
    printf("%d\n", num1);
    printf("%d\n", num2);
    printf("%d\n", num3);
    // Display numbers with width of 5 (right-aligned by default)
    printf("%5d\n", num1);
    printf("%5d\n", num2);
    printf("%5d\n", num3);
    // Display numbers with width of 5 (left-aligned)
    printf("%-5d\n", num1);
    printf("%-5d\n", num2);
    printf("%-5d\n", num3);
    // Display numbers with leading zeros and width of 5
    printf("%05d\n", num1);
    printf("%05d\n", num2);
    printf("%05d\n", num3);
    // Display numbers with positve sign and width of 5
    printf("%+5d\n", num1);
    printf("%+5d\n", num2);
    printf("%+5d\n", num3);

    /* Precision Examples */

    float price1 = 19.99;
    float price2 = 1.50;
    float price3 = -100.00;

    // Display prices
    printf("%f\n", price1);
    printf("%f\n", price2);
    printf("%f\n", price3);
    // Display prices with 2 decimal places
    printf("%.2f\n", price1);
    printf("%.2f\n", price2);
    printf("%.2f\n", price3);
    // Examples with flags
    printf("%+8.2f\n", price1); // Width of 8, 2 decimal places, always show sign
    printf("%+8.2f\n", price2); // Width of 8, 2 decimal places, always show sign
    printf("%+8.2f\n", price3); // Width of 8, 2 decimal places, always show sign

    return 0;
}