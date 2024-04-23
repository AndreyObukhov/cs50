// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>

#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 70000;

// Hash table
node *table[N];
int WordsCounter = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int len = strlen(word);
    char WordCopy[len + 1];
    int HashNumber;

    for (int i = 0; i < len + 1; i++)
    {
        WordCopy[i] = tolower(word[i]);
    };
    HashNumber = hash(WordCopy);

    for (node *tmp = table[HashNumber]; tmp != NULL; tmp = tmp->next)
    {
        if (strcmp(tmp->word, WordCopy) == 0) //strcasecmp
        {
            return true;
        };
    };

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int len = strlen(word);
    unsigned long int HashNumber = 0;

    for (int i = 0; i < len + 1; i++)
    {
        HashNumber = HashNumber * 10 + (int) word[i];
    };
    return HashNumber % N;
    // return toupper(word[0]) - 'A';
};

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *WORDS = fopen(dictionary, "r");
    if (WORDS == NULL)
    {
        return false;
    };
    char word[LENGTH + 1];
    unsigned int HashNumb;
    while (fscanf(WORDS, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(WORDS);
            return false;
        };
        strcpy(n->word, word);
        n->next = NULL;
        HashNumb = hash(word);

        n->next = table[HashNumb];
        table[HashNumb] = n;

        WordsCounter++;
    };
    // Allocate memory for one node
    // node *n = malloc(sizeof(node));
    // strcpy(n->word, "Hello"); // Add word "Hello" to the node
    // n->next = NULL; // Set the pointer of the new node to NULL
    fclose(WORDS);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return WordsCounter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    node *tmp1 = NULL;
    node  *tmp2 = NULL;
    for (unsigned int i = 1; i < N; i++)
    {
        tmp1 = table[i];
        while (tmp1 != NULL)
        {
            tmp2 = tmp1;
            tmp1 = tmp1->next;
            free(tmp2);
        };
    };
    return true;
}
