import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")

    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    output = {}
    # Number of pages for which current page has links
    num_links = len(corpus[page])
    # Number of all pages in the corpus
    num_pages = len(corpus)

    # Probability 1 is for pages for which our current page has not links
    Prob1 = (1 - damping_factor) / num_pages
    # Probability 2 is for pages for which our current page has links (it is zero for zero linked pages)
    if num_links != 0:
        Prob2 = damping_factor / num_links
    else:
        Prob2 = 0

    for CurrentPage in corpus:
        # If page has no outgoing links:
        if num_links == 0:
            output[CurrentPage] = 1 / num_pages
        # If page has some outgoing links:
        else:
            # Probability for link this page has:
            if CurrentPage in corpus[page]:
                output[CurrentPage] = Prob1 + Prob2
            # Probability for all other pages:
            else:
                output[CurrentPage] = Prob1

    return output


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Pages is number of all pages in the corpus
    pages = list(corpus)
    output = {}

    for i in pages:
        output[i] = 0
    random.seed()

    # The first sample is generated by choosing from a page at random.
    CurrentPage = random.choice(pages)
    output[CurrentPage] = 1 / n

    # Other n - 1 samples:
    for j in range(1, n):
        sample = transition_model(corpus, CurrentPage, damping_factor)
        # Sample pages is list of pages with link on the current page
        samplePages = list(sample)
        # Sample probabilities is list (vector) for pages in samplePages
        sampleProbs = list(sample.values())
        # We randomly choose one page:
        CurrentPage = random.choices(samplePages, sampleProbs)[0]
        output[CurrentPage] += 1 / n

    return output


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    PR_copy = {}
    PR = {}
    N = len(corpus)
    for page in corpus:
        PR[page] = 1 / N

    lagest_deviation = 1
    while lagest_deviation >= 0.001:
        PR_copy = PR.copy()
        lagest_deviation = 0
        for page in PR:
            # Related pages are pages with link to this current page.
            related_pages = [link for link in corpus if page in corpus[link]]
            # Now count the first part of the PageRank formula
            PR[page] = (1 - damping_factor) / N
            # SUM will be the second part
            SUM = []
            if len(related_pages) != 0:
                for CurrentPage in related_pages:
                    SUM.append(PR_copy[CurrentPage] / len(corpus[CurrentPage]))
            # Overall PR for page will be:
            PR[page] += damping_factor * sum(SUM)
            
            # We check if PageRank value changes by more than 0.001
            deviation = abs(PR[page] - PR_copy[page])
            if deviation > lagest_deviation:
                lagest_deviation = deviation
    # Normalization of the values' vector
    norma = sum(PR.values())
    for page in PR:
        PR[page] /= norma
    return PR


if __name__ == "__main__":
    main()