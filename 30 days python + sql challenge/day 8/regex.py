import sys

sys.path.append("../day 4")

from search import matchRegex
# ************* Metacharacters ***************

# 1. Escaping metacharacters using '\'
match = matchRegex("\.", "my name is omkar.")  # as . is a metacharacter, we need to add \ in front of it

# 2. special character classes
import specialCharacterClasses

# 3. anchors

# ^ : matches with start
match = matchRegex(r"^omkar", "omkar sase")

# $ : matches with end
match = matchRegex(r"sase$", "omkar sase")

# 4. Quantifiers
# *,+,.,{}

# 5. Grouping & alteration
match = matchRegex(r"(abc|def)", "abcdf")   # matches either 'abc' or 'def'
match = matchRegex(r"(abc|def)", "asdfsdef")
