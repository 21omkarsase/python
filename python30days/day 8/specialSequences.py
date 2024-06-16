import sys

sys.path.append("../day 4")
from search import matchRegex


# /A : matches start of a string

# /b : matches with either start or end based on it's positioning
match = matchRegex(r"\b21", "21omkarsase" # end_part\b or end_part\Z
match = matchRegex(r"21\b", "omkarsase21")

# /B : matches if pattern occurs not at word boundaries
match = matchRegex(r"21","omkar21sase")
