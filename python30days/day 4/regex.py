import re
import search

# powerful tools for pattern matching in strings.
# search for, extract, and manipulate text based on patterns.

# 1 Literal Characters -> matches with itself in the text
pattern = "Omkar"
text = "my name is Omkar"

match = search.matchRegex(pattern, text)

# 2. Metacharacter
print("Meta characters")

# . -> matches any character except newline
pattern = "a.b"
text1 = "axb"
text2 = "adxb" # more than one char

match = search.matchRegex(pattern, text1)
match = search.matchRegex(pattern, text2)

print("\n")

# * -> matches zero or more characters of preceding charcter
# The pattern ab* matches any string that starts with a, followed by 0 or more occurrences of b.
pattern = "ab*"
text1 = "ba"
text2 = "ab"

text3 = "abbv"

match = search.matchRegex(pattern, text1)
match = search.matchRegex(pattern, text2)
print('alf')
match = search.matchRegex(pattern, text3)

print("\n")

# + -> matches 1 more occurences of preceding character
# The pattern ab+ matches any string that starts with a, followed by 1 or more occurrences of b.

pattern = "ab+"
text0 = 'a'

match = search.matchRegex(pattern, text0)
match = search.matchRegex(pattern, text1)
match = search.matchRegex(pattern, text2)
match = search.matchRegex(pattern, text3)

print("\n")

# question mark -> matches 0 or 1 occurrences of preceding character

pattern = "ab?"

match = search.matchRegex(pattern, "a")
match = search.matchRegex(pattern, "ab")
match = search.matchRegex(pattern, "bc")