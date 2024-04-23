#include <stdio.h>
#include <cs50.h>

//Prints output piramid
void Output(int Input)
{
    for (int a = 1; a < Input + 1; a++)
    {
        for (int c = Input - a; c > 0; c--)
        {
            printf(" ");
        }
        for (int b = 1; b < a + 1; b++)
        {
            printf("#");
        }
        printf("  ");
        for (int b = 1; b < a + 1; b++)
        {
            printf("#");
        }
        printf("\n");
    }
}

//main function
int main(void)
{
    int Input = 0;
    do
    {
        Input = get_int("Height: ");

    }
    while (Input < 1 || Input > 8);
    Output(Input);
}