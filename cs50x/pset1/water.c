#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int Input = get_int("/waterminutes: ");
    printf("bottles: %i\n", Input*12);
}