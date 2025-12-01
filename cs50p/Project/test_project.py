import wikipedia
import random
from random_word import RandomWords
from pyfiglet import Figlet
import project


def main():
    # test_find_article()
    test_find_random_name()
    test_clear_page()


def test_find_article():
    # Exaple with exact Wikipedia page (as of 5 July 2024)
    assert (
        project.find_article(wikipedia.page("The Fugitive (1920 film)"))
        == "The Fugitive (French: La Fugitive) is a 1920 French silent film directed by André Hugon and starring Marie-Louise Derval, André Nox and Armand Numès.\n\n== Cast ==\nMarie-Louise Derval\nAndré Nox\nArmand Numès\nJane Renouardt\nPierre Denols\nAdrienne Duriez\n\n== References ==\n\n== Bibliography ==\nRège, Philippe. Encyclopedia of French Film Directors, Volume 1. Scarecrow Press, 2009.\n\n== External links ==\nThe Fugitive at IMDb"
    )


def test_find_random_name():
    try:
        name = project.find_random_name()
        wikipedia.page(name)
    except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError):
        pass


def test_clear_page():
    assert project.clear_page("A\n\n\nA") == "A\n\nA"
    assert project.clear_page("A\nA\nA") == "A\nA\nA"


if __name__ == "__main__":
    main()
