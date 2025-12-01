"""
Program prompts the user for a greeting. If the greeting starts with “hello”, output $0.
If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100.
Ignore any leading whitespace in the user's greeting, and treat the user's greeting case-insensitively.
"""
def main():
    Input = input("Greeting: ")
    print(Output(Input))

def Output(Input):
    Input = Input.lower().strip()
    if Input.startswith("hello"):
        return("$0")
    if Input.startswith("h"):
        return("$20")
    return("$100")


main()
