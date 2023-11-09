import re
import  sys
sys.path.append("../day 4")

from search import matchRegex

# match email
email_pattern = r"^[0-9a-zA-Z._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
match = matchRegex(email_pattern, "saseomkar214@gmail.com")
match = matchRegex(email_pattern, "saseomkar214@gmail.c")

# extract urls
url_pattern = r"http[s]?://[a-zA-Z0-9./]+"
match = matchRegex(url_pattern, "my website name is https://omkarsase.com")
print(re.findall(url_pattern, "my website name is https://omkarsase.com y website name is https://omkarsase.c"))
