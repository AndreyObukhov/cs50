import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    # We initialize joint probability which we want to calculate:
    joint_prob = 1

    # For all people do:
    for current_person in people:
        current_prob = 1
        current_gene = (2 if current_person in two_genes else 1 if current_person in one_gene else 0)
        current_trait = current_person in have_trait

        mother = people[current_person]["mother"]
        father = people[current_person]["father"]

        # If person has no parents:
        if not mother and not father:
            current_prob *= PROBS["gene"][current_gene]
        else:
            # If person has parent(s):
            mother_prob = (1 - PROBS["mutation"] if mother in two_genes else 0.5 if mother in one_gene else PROBS["mutation"])
            father_prob = (1 - PROBS["mutation"] if father in two_genes else 0.5 if father in one_gene else PROBS["mutation"])

            if current_gene == 2:
                current_prob *= mother_prob * father_prob
            elif current_gene == 1:
                current_prob *= mother_prob * (1 - father_prob) + (1 - mother_prob) * father_prob
            else:
                current_prob *= (1 - father_prob) * (1 - mother_prob)

        # We also consider probability of having the trait (for particular genes combination):
        current_prob *= PROBS["trait"][current_gene][current_trait]

        # We are multiplying overall joint probability be the particular current person's probability:
        joint_prob *= current_prob

    return joint_prob


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    # For all people do:
    for current_person in probabilities:
        current_gene = (2 if current_person in two_genes else 1 if current_person in one_gene else 0)
        current_trait = current_person in have_trait
        # We just add a new joint probability `p`:
        probabilities[current_person]["gene"][current_gene] += p
        probabilities[current_person]["trait"][current_trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    # For all people do:
    for current_person in probabilities:
        # We have to divide particular probability by the sum of all probabilities (i.e. normalize it):
        SUM = sum(probabilities[current_person]["gene"][i] for i in range(0, 3))
        for i in range(0, 3):
            probabilities[current_person]["gene"][i] /= SUM
        SUM = probabilities[current_person]["trait"][True] + probabilities[current_person]["trait"][False]
        probabilities[current_person]["trait"][True] /= SUM
        probabilities[current_person]["trait"][False] /= SUM


if __name__ == "__main__":
    main()
