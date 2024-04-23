import nltk
import sys
import os
import string
import numpy
from functools import reduce

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    output = {}

    # Make platform-independent file path
    CurrentPath = os.path.join(f'{directory}')

    # Loop and read all txt documents with UTF-8 encoding
    for filename in os.listdir(CurrentPath):
        if filename.endswith('.txt'):
            f = open(os.path.join(f'{CurrentPath}', f'{filename}'), 'r', encoding="utf8")
            output[filename] = f.read()
            f.close()

    return output


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    # nltk.download('stopwords')
    # nltk.download('punkt')
    # Performing tokenization and making each word a lowercased string
    input = nltk.word_tokenize(document.lower())
    output = []

    # Tokenize with excluding stopwords and punctuation
    for word in input:
        if word not in set(nltk.corpus.stopwords.words("english")) | set(string.punctuation):
            output.append(word)

    return output


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    # IDF is output dict, sets will contain set of words for each document, main_set is the union of all sets
    IDF = {}
    sets = []
    main_set = set()
    TOTAL_DOCUMENTS = len(documents)

    # Loop through all documents and complete sets
    for document in documents:
        s = set(documents[document])
        sets.append(s)
        main_set = main_set | s

    # Calculate number of docs containing each word (NDM) and IDF
    for word in main_set:
        NDM = 0
        for document in sets:
            if word in document:
                NDM += 1
        IDF[word] = numpy.log(TOTAL_DOCUMENTS / NDM)

    return IDF


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """

    # Dictionary to hold tf-idfs for files
    files_tfidf = {filename: 0 for filename in files}

    # Loop through all words in query:
    for word in query:
        # Use only words from idfs:
        if word in idfs:
            # Loop through all files, count tf-idf for each file:
            for file in files:
                tf = files[file].count(word)
                tf_idf = tf * idfs[word]
                files_tfidf[file] += tf_idf
    # Sort all files from highest tf-idf to lowest
    files_sorted = sorted([file for file in files], key=lambda x: files_tfidf[x], reverse=True)

    # Return first n files from sorted list
    return files_sorted[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density (QTD).
    """

    # Dictionary for storing information needed for calculation purposes:
    # Len ... Lenght of sentence after tokenize process
    # query_words ... Number of words being both in the sentence and in the query
    info_sentence = {sentence: {'len': 0, 'query_words': 0, 'IDF': 0, 'QTD': 0} for sentence in sentences}

    # Loop through all sentences:
    for sentence in sentences:
        s = info_sentence[sentence]
        s['len'] = len(sentences[sentence])
        # Loop through all words in query:
        for word in query:
            # If query word is in sentence, update its score
            if word in sentences[sentence]:
                s['IDF'] += idfs[word]
                s['query_words'] += sentences[sentence].count(word)

        # Calculate QTD for all sentences:
        s['QTD'] = s['query_words'] / s['len']

    # Sort all sentences by IDF firstly and by QTD secondly (if IDF values are equal)
    sorted_sentences = sorted([sentence for sentence in sentences], key=lambda x: (
        info_sentence[x]['IDF'], info_sentence[x]['QTD']), reverse=True)

    # Return first n sentences:
    return sorted_sentences[:n]


if __name__ == "__main__":
    main()
