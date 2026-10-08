#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>

int main()
{
    float lap = 5, distance = 14;

    printf("Diketahui :\n");
    printf("Pak Dengklek mengelilingi taman = %.0f Putaran\n", lap);
    printf("Jarak tempuh Pak Dengklek = %.0f Kilometer\n", distance);
    printf("\n");

    float circumference = distance / lap;
    float radius = circumference / (2 * M_PI);
    
    printf("Jawaban :\n");
    printf("Jari-jari taman yang dikelilingi Pak Dengklek adalah %.2f Kilometer\n", radius);
    return 0;
}