#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

//Global array (26x2)x2 consists of upper and lower letters in alphabetical order (first column)
//and corresponding upper and lower letters in the order given by the key.
char PERMUTATION[26 * 2][2];

//Function returns true if key consists of all 26 characters of alphabet
bool characters(void)
{
    int z[26];
    for (int i = 0; i < 26; i++)
    {
        z[i] = 1;
        for (int j = 0; j < 26; j++)
        {
            if (PERMUTATION[j][1] == 'A' + i)
            {
                z[i] = 0;
            }
        }
    };
    for (int i = 0; i < 26; i++)
    {
        if (z[i] == 1)
        {
            return (false);
        };
    };
    return (true);
};

//Main body of program
int main(int argc, string argv[])
{
    //We are checking number of input keys.
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    //Also we are checking number of chars in the input key.
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    //Now we are making cipherarray from the key.
    for (int i = 0; i < 26; i++)
    {
        PERMUTATION[i][0] = 'A' + i;
        PERMUTATION[i][1] = toupper(argv[1][i]);
        PERMUTATION[i + 26][0] = PERMUTATION[i][0] + 'a' - 'A';
        PERMUTATION[i + 26][1] = PERMUTATION[i][1] + 'a' - 'A';
    }

    //We are checking if there are all 26 letters in the key.
    if (characters() == false)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    };

    //We are reading text.
    string INPUT = get_string("plaintext: ");

    printf("ciphertext: ");
    //We are construct output text by using prepared matrix PERMUTATION[26*2][2]
    for (int i = 0; i < strlen(INPUT); i++)
    {
        if (isalpha(INPUT[i]) == false)
        {
            printf("%c", INPUT[i]);
        }
        else
        {
            for (int j = 0; j < 26 * 2; j++)
            {
                if (PERMUTATION[j][0] == INPUT[i])
                {
                    printf("%c", PERMUTATION[j][1]);

                };

            };
        };
    };
    printf("\n");
}