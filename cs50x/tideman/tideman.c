#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
bool cycle(int start, int finish);
bool cycle(int winner, int loser);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        printf("\n");

        record_preferences(ranks);
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    //We search the name in the list of candidates.
    //If the name is found, we assgin this name's position (in the array candidates[MAX]) to variable ranks[rank]
    //and return true.
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i]) == 0)
        {
            ranks[rank] = i;
            return true;
        };
    };
    //If the name is not found in the list of candidates, we return false.
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            preferences[ranks[i]][ranks[j]]++;
        };
    };
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    pair_count = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i])
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count++;
            };
        };
    };
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    pair clipboard;
    int k;
    for (int i = 0; i < pair_count; i++)
    {
        k = i;
        for (int j = i; j < pair_count - 1; j++)
        {
            if (preferences[pairs[j + 1].winner][pairs[j + 1].loser] > preferences[pairs[k].winner][pairs[k].loser])
            {
                k = j + 1;
            }
            else
            {
                if (preferences[pairs[j + 1].winner][pairs[j + 1].loser] == preferences[pairs[k].winner][pairs[k].loser] &&
                    preferences[pairs[j + 1].loser][pairs[j + 1].winner] < preferences[pairs[k].loser][pairs[k].winner])
                {
                    k = j + 1;
                };
            };
        };
        clipboard = pairs[i];
        pairs[i] = pairs[k];
        pairs[k] = clipboard;
    };
    return;
}

bool cycle2(int start, int finish)
{
    if (locked[start][finish])
    {
        return true;
    };

    for (int i = 0; i < candidate_count; i++)
    {
        if (locked[start][i])
        {
            return cycle(i, finish);
        };
    };
    return false;
};

bool cycle(int finish, int start)
{
    while (finish != -1 && finish != start)
    {
        bool found = false;
        for (int i = 0; i < candidate_count; i++)
        {
            if (locked[i][finish])
            {
                found = true;
                finish = i;
            }
        }
        if (!found)
        {
            finish = -1;
        }
    }
    if (finish == start)
    {
        return true;
    }
    return false;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for (int i = 0; i < pair_count; i++)
    {
        if (!cycle(pairs[i].winner, pairs[i].loser))
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        };
    };
    return;
}

// Print the winner of the election
void print_winner(void)
{
    bool WINNER[MAX];
    for (int i = 0; i < candidate_count; i++)
    {
        WINNER[i] = true;
    };
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[i][j])
            {
                WINNER[j] = false;
            };
        };
    };
    for (int i = 0; i < candidate_count; i++)
    {
        if (WINNER[i])
        {
            printf("%s\n", candidates[i]);
        };
    };
    return;
}

