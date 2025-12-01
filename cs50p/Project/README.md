```
Andrey Obukhov
Harvard's CS50P July 2024
Final Project
```
# Reading Wikipedia pages in terminal
#### Video Demo:  https://youtu.be/hMLng0CdKiM
## Description
There are a lot of ways to get access to Wikipedia using different Python libraries. For the purpose of this project we will use one of them: **wikipedia 1.4.0**. Our aim is to get the opportunity to extract plain text from Wikipedia pages and read them without web browser. Current project implemented following features:
* Set up any preferable language to search in
* Show most relevant search result for a particular request
* Open and read Wikipedia article in terminal as a plain text
* Requst a random Wikipedia page

Program uses **pyfiglet** lybrary for show page heading. Default language is set up to English. Random pages is shown for plain or "random" entered pages names.

## How to work with program
* Firstly, we are requested to choose language (using ISO language code). English is used as default.
* Second step is to enter search request and obtain most relevant search results on the output list. We can skip this step by hitting Enter.
* Third step is to input **exact Wikipedia page name**. For blank or "random" request random page will be shown. For irrelevant or non existing pages we will be prompted to reinput request (more precisely, **special exceptions** will be raised).
* Finally, Wikipedia page with Figlet header will be shown in terminal. That's how program ends.

## Used libraries
### wikipedia 1.4.0
As was mentioned before, main external library used in this project is **wikipedia 1.4.0**. This library takes Wikipedia pages as objects with range of useful methods. We can, for instance get URL, name or images for particular page. For the purpose of this project, most important method is **content**, it outputs a str object, so we can print it using standard Python function.
### random_word and random
Another feature implemented in this project is opportunity to request random Wikipedia article. Under the hood it uses two randomizer: main is **random_word**, which generates exact one random word for us. Definitely, we cannot be sure that Wikipedia contains page named after this word, function **wikipedia.search** helps us: it return list of string with most relevant search results for the requested word. Then we choose randomly (with library **random**) one of these results and determine it as name for random page to output in terminal.
### pyfiglet
 It takes ASCII text and renders it in ASCII art fonts for page header. This library in detail described in the **CS50P** course.

## Special exceptions
This project also contains special exceptions:
* **wikipedia.exceptions.PageError**, when Wikipedian pages with requested name dosn't exist;
* **wikipedia.exceptions.DisambiguationError**, when the page exists, but it is a *disambiguation page*

## Possible improvements
One of the main and evident improvements could be made in this project is opportunity to save downloaded Wikipedia page as a text file. Also, it is possible to implement illustrations from original webpages.
