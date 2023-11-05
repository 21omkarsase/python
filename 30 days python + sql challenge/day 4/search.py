import re
def matchRegex(pattern, text):
    match = re.search(pattern, text)

    if match != None:
        print("Start : ", match.span()[0], " <-->", "End : ", match.span()[1])
    else:
        print("No match found")

    return match