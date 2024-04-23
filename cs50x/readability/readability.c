#include <stdio.h>
#include <math.h>
#include <ctype.h>

int main(void)
{
    float letters = 0, words = 0, sentences = 0;
    char c;
    printf("Text: ");
    do
    {
        scanf("%c", &c);
        //We read each character one by one and determine if it is a letter, end of a word, end of a sentence or non.
        if isalpha(c)
        {
            letters++;
        }
        else
        {
            if (c == ' ')
            {
                words++;
            }
            else
            {
                if ((c == '.') || (c == '!') || (c == '?'))
                {
                    sentences++;

                };
            };
        };
    }
    //\n means end of the whole text
    while (c != '\n');
    //We must add one more word to a counter. It was not considered by a program.
    words++;
    //Now we are counting values L, S and final value of index.
    float L = letters * 100 / words, S = sentences * 100 / words;
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    //Printing results.
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        if (index > 15)
        {
            printf("Grade 16+\n");
        }
        else
        {
            printf("Grade %i\n", index);
        }
    }
}