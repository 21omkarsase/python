import sys

sys.path.append("../day 4")

from search import matchRegex

match = matchRegex("[aeiou]", "omkar")  # will match any one character in text string

# Quantifiers
match = matchRegex("ab{1}", "abb") # will match exactly n characters of preceding character
match = matchRegex("ab{2,}", "abbbbb") # matches 'ab' followed by 2 or more b
match = matchRegex("ab{2,4}", "sdfdf abbbbbbbb") # matches

# Anchors
match = matchRegex("^omkar", "omkar - sase") # will match only if 'omkar' is present at beginning

# Groups and Alternation:
match = matchRegex("(ab)+", "babab") # will match one or more occurences of ab

# Lookahead and Lookbehind
match = matchRegex("ab(?=cde)", "abcdefg") # will match only if ab is followed by cde

# Character Classes and Negation

match = matchRegex("[0-9]", "omkar21") # matches any single numerical character
match = matchRegex("[a-zA-Z]", "21 omkar") # matches any single alphabetical character
match = matchRegex("[^0-9]", "21Hero") # matches any single non digit character
match = matchRegex("[^a-zA-Z]", "21Hero") # matches any single non-alphabetic character













