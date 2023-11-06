import re
import sys

sys.path.append("../day 4")

from search import matchRegex

# Regular Expressions Functions
# 1. findall()  -> returns a list containing all matches

matches = re.findall("ai", "The rain in spain")
print(matches) # ['ai', 'ai']

# 2. search

# 3. split() -> return a list where string has been split at each time
splitted_list = re.split("\d", "The rai4n in S2pain")
print(splitted_list)

# 4. sub() -> replces matches with text
res = re.sub("\s", " space ", "The rain in Spain")
print(res)

# match object
match = matchRegex("ai", "the rain in Spain")
print(match.span()[0])
print(match.string)
print(match.group())