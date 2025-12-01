"""
Program prompts the user for the name of a file and then outputs that file's media type
if the file's name ends, case-insensitively, in any of appropriate suffixes.
"""
def main():
    name = input("File name: ")
    print(Output(name))

def Output(name):
    name = name.lower().strip()
    if name.endswith((".jpeg", ".jpg")):
        return("image/jpeg")
    if name.endswith(".gif"):
        return("image/gif")
    if name.endswith(".png"):
        return("image/png")
    if name.endswith(".pdf"):
        return("application/pdf")
    if name.endswith(".txt"):
        return("text/plain")
    if name.endswith(".zip"):
        return("application/zip")
    return("application/octet-stream")

main()