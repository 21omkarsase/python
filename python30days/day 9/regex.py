import sys

sys.path.append("../day 4")

from search import matchRegex

# [arn] -> matches with any one char among 'arn'
match = matchRegex(r"[arn]", "my name is arn")

# [^arn] -> match for any one char except charcter from 'arn'
match = matchRegex(r"[^arn]", "zzzz df arn is my name")

# [0-5][0-9]
match = matchRegex(r"[0-5][0-9]", "my roll number is 21")
print(match.group())

# [+] -> match for + character
match = matchRegex(r"[+]", "21 + 4")