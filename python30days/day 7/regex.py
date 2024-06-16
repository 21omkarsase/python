import re


# Regular Expressions Functions
# 1. findall()  -> returns a list containing all matches

matches = re.findall("ai", "The rain in spain")
print(matches) # ['ai', 'ai']

# 2. search

# 3. split() -> return a list where string has been split at each time
splitted_list = re.split("h", "The rai4n in S2pain")
print(splitted_list)

# 4. sub() -> replces matches with text
res = re.sub("h", " space ", "The rain in Spain")
print(res)

# match object
# match = matchRegex("ai", "the rain in Spain")
# print(match.span()[0])
# print(match.string)
# print(match.group())