import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # Reading data from the file
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        evidence = []
        labels = []
        for row in reader:
            evidence.append([cell for cell in row[:17]])
            labels.append(int(0) if row[17] == 'FALSE' else int(1))

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # We set each type as prescribed
    for row in evidence:
        row[0] = int(row[0])
        row[1] = float(row[1])
        row[2] = int(row[2])
        row[3] = float(row[3])
        row[4] = int(row[4])
        row[5] = float(row[5])
        row[6] = float(row[6])
        row[7] = float(row[7])
        row[8] = float(row[8])
        row[9] = float(row[9])
        row[10] = months.index(row[10])
        row[11] = int(row[11])
        row[12] = int(row[12])
        row[13] = int(row[13])
        row[14] = int(row[14])

        if row[15] == 'Returning_Visitor':
            row[15] = int(1)
        else:
            row[15] = int(0)

        if row[16] == 'TRUE':
            row[16] = int(1)
        else:
            row[16] = int(0)

    return(evidence, labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    # Using nearest-neighbour classification algorithm in scikit-learn package
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    sum = len(labels)
    ActualPositive = 0
    ActualNegative = 0
    CorrectPositive = 0
    CorrectNegative = 0

    # We count actual labels and accurately identified labels in the loop
    for i in range(sum):
        if labels[i] == 1:
            ActualPositive += 1
            if predictions[i] == 1:
                CorrectPositive += 1
        else:
            ActualNegative += 1
            if predictions[i] == 0:
                CorrectNegative += 1

    # We calculate required parameters
    sensitivity = float(CorrectPositive / ActualPositive)
    specificity = float(CorrectNegative / ActualNegative)

    return sensitivity, specificity


if __name__ == "__main__":
    main()
