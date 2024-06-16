import sys

sys.path.append("../day 4")

from search import matchRegex
# ************* Metacharacters ***************

# 1. Escaping metacharacters using '\'
match = matchRegex("\.", "my name is omkar.")  # as . is a metacharacter, we need to add \ in front of it

# 2. special character classes

# \d : matches with decimal digit
match = matchRegex("\d", "omkarsase21")

# \D : matches any non-digit
match = matchRegex("\D", "21omkarsase")

# \w : matches any word character
match = matchRegex("\w", "@21_omkarsase") # alphanumeric + underscore

# \W : matches any non-word character
match = matchRegex("\W", "21@omkarsase")

# \s : matches any whitespace character
match = matchRegex(r"\s", "omkar sase")

# \S : matches with non-space characters
match = matchRegex(r"\S", "   omkar sase")