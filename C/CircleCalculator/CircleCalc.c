#include <stdio.h>
#include <math.h>

int main()
{
    // Initialize variables
    double radius = 0.0;
    double area = 0.0;
    double surfaceArea = 0.0;
    double volume = 0.0;
    const double PI = 3.14159;

    printf("Enter the radius of the circle: ");
    scanf("%lf", &radius);

    // Calculate area of the circle
    area = PI * pow(radius, 2.0);

    // Correct surface area of the sphere
    surfaceArea = 4 * PI * pow(radius, 2.0);

    // Correct volume of the sphere
    volume = (4.0 / 3.0) * PI * pow(radius, 3.0);

    printf("Area of the circle: %.2lf\n", area);
    printf("Surface area of the sphere: %.2lf\n", surfaceArea);
    printf("Volume of the sphere: %.2lf\n", volume);
    
    return 0;
}