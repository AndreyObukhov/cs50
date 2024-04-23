#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    // Makes variables for input and its copy.
    long long CardNumber = get_long_long("Number: ");
    long long CardNumberCopy = CardNumber;

    // If input has more than 16 digits, card is invalid.
    if (trunc(CardNumber / pow(10, 16)) > 0)
    {
        printf("INVALID\n");
        return (0);
    };

    // Calculates sum using Luhn’s algorithm.
    int sum = 0, digit;
    for (int i = 1; i < 17; i++)
    {
        if (i % 2 == 1)
        {
            sum += CardNumberCopy % 10;
        }
        else
        {
            digit = (CardNumberCopy % 10) * 2;
            sum += (digit % 10) + trunc(digit / 10);
        }
        CardNumberCopy = trunc(CardNumberCopy / 10);
    };

    // Checks conditions and prints result.
    if (sum % 10 != 0)
    {
        printf("INVALID\n");
        return (0);
    };
    if (trunc(CardNumber / pow(10, 15)) == 4)
    {
        printf("VISA\n");
        return (0);
    };
    if (trunc(CardNumber / pow(10, 12)) == 4)
    {
        printf("VISA\n");
        return (0);
    };
    if ((trunc(CardNumber / pow(10, 14)) >= 51) && (trunc(CardNumber / pow(10, 14)) <= 55))
    {
        printf("MASTERCARD\n");
        return (0);
    };
    if ((trunc(CardNumber / pow(10, 13)) == 34) || (trunc(CardNumber / pow(10, 13)) == 37))
    {
        printf("AMEX\n");
        return (0);
    };
    printf("INVALID\n");
    return (0);
}