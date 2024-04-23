import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py database.csv sequence.txt")

    # Read database file into a variable
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        # InputHeader = []
        # InputHeader = next(reader)
        # print(InputHeader)
        database = []
        for row in reader:
            database.append(row)

        for i in range(1, len(database)):
            for j in range(1, len(database[0])):
                database[i][j] = int(database[i][j])

    # Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as file:
        DNA = file.read()

    # Find longest match of each STR in DNA sequence
    LongestMatch = []
    for STR in range(1, len(database[0])):
        LongestMatch.append(longest_match(DNA, database[0][STR]))

    # Check database for matching profiles
    for name in range(1, len(database)):
        if database[name][1:] == LongestMatch:
            print(database[name][0])
            exit(0)
    print("No match")
    exit(1)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
