#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Input of start size of population
    int start = 0;
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);

    //Input of end size of population
    int end = 0;
    do
    {
        end = get_int("End size: ");
    }
    while (end < start);
    
    //Calculation of required amount of years
    int years = 0;
    while (start < end)
    {
        start = start + start / 3 - start / 4;
        years++;
    };

    printf("Years: %i\n", years);
}