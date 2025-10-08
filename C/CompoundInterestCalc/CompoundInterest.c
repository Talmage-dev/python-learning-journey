#include <stdio.h>
#include <math.h>

int main()
{
    // Compound Interest Claculator

    // Initialize variables
    double principal = 0.0; // Initial amount of money
    double rate = 0.0; // Annual interest rate
    int years = 0; // Number of years the money is invested
    int times = 0; // Number of times interest is compounded per year
    double total = 0.0; // Total amount after interest

    printf("Compound Interest Calculator\n");

    // Get user input
    printf("Enter the principal amount (P): ");
    scanf("%lf", &principal);

    printf("Enter the annual interest rate as a percentage (r): ");
    scanf("%lf", &rate);
    rate /= 100; // convert pecentage to a decimal value

    printf("Enter the number of years the money will be invested (t): ");
    scanf("%d", &years);

    printf("Enter the number of time interest compounded per year (n): ");
    scanf("%d", &times);

    // Calculate compound interest
    total = principal * pow((1 + rate / times), times * years);

    // Display the result
    printf("With an intial investment of $%.2lf and after %d years invested, you will have: $%.2lf\n", principal, years, total);

    return 0;
}