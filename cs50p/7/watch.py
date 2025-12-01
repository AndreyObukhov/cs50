import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    """
    Expects a str of HTML as input, extracts any YouTube URL that’s the value of a src attribute of
    an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str.
    Assume that the value of src will be surrounded by double quotes. And assume that the input will
    contain no more than one such URL. If the input does not contain any such URL at all, return None.
    """
    suffix = re.sub(r"^<iframe.*? src=(\"https?://)?(www\.)?youtube\.com/embed/", "", s)
    if suffix == s:
        return None
    return f"https://youtu.be/{suffix[0:suffix.find('"')]}"


if __name__ == "__main__":
    main()
