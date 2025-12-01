import wikipedia
import random
from pyfiglet import Figlet
from random_word import RandomWords


def main():
    # Set preferable Wikipedia language
    while True:
        lang = input("Please choose your language using ISO language code: ")
        if lang in wikipedia.languages():
            break
        elif lang == "":
            lang = "en"
            break
    wikipedia.set_lang(lang)

    while True:
        # get list of the exact Wikipedia pages by request
        request = input("Your request: ")
        if request == "":
            break
        search_results = wikipedia.search(request)
        print("Search results:", end="")
        for result in search_results:
            print(f" {result},", end="")
        print(f"\nDo you want to search more? Type 'Yes' if so: ", end="")
        if input().lower() not in {"yes", "y"}:
            break

    # get the exact article object
    while True:
        try:
            name = input(
                "Please enter exact Wikipedia page title you are searching for: "
            )
            if name.lower() in ["random", ""]:
                name = find_random_name()
            page = wikipedia.page(name)
            break
        except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError):
            print(f"Page with the name '{name}' does not exist, try another name.")
    page_str = find_article(page)
    # print page title with pyfiglet
    f = Figlet(font="standard")
    print(f.renderText(name), end = "")
    # print Wikipedia page, cleared from excessive newline symbols
    print(clear_page(page_str))


def find_random_name():
    """Find a random name of existing Wikipedia page and return it as the string"""
    r = RandomWords()
    while True:
        search_results = wikipedia.search(r.get_random_word())
        if search_results != []:
            return random.choice(search_results)

def find_article(page):
    """Find an article in Wikipedia and return it as the string"""

    # content is a full page str
    content = page.content
    return content


def clear_page(page):
    """Make a str of the Wikipedia page more suitable for reading from the terminal"""
    clr_page = ""
    # get rid of excessive newline symbols
    lenght = len(page)
    for i in range(lenght - 2):
        if (
            page[i] == "\n"
            and page[i + 1] == "\n"
            and page[i + 2] != "\n"
            or page[i] == "\n"
            and page[i + 1] != "\n"
            or page[i] != "\n"
        ):
            clr_page += page[i]
    return clr_page + page[lenght - 2:]


if __name__ == "__main__":
    main()
