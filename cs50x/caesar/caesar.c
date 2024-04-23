#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    //We are checking number of input keys.
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    };

    //We are checking if the key is integer.
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (isdigit(argv[1][i]) == false)
        {
            printf("Usage: ./caesar key\n");
            return (1);
        };
    }

    //k is our key
    int k = atoi(argv[1]);
    //INPUT is the text we want to cipher.
    string INPUT = get_string("plaintext:  ");
    printf("ciphertext: ");
    //We use formula c_i = (p_i + k) % 26 separately for upper and lower letters.
    for (int i = 0; i < strlen(INPUT); i++)
    {
        if (isalpha(INPUT[i]))
        {
            if (isupper(INPUT[i]))
            {
                printf("%c", ((INPUT[i] - 'A' + k) % 26) + 'A');
            }
            else
            {
                printf("%c", ((INPUT[i] - 'a' + k) % 26) + 'a');
            }
        }
        else
        {
            //If it is not an alphabetic character, we simply copy it.
            printf("%c", INPUT[i]);
        }
    }
    printf("\n");
    return (0);
}