import re
import searchLiteral

# powerful tools for pattern matching in strings.
# search for, extract, and manipulate text based on patterns.

# 1 Literal Characters -> matches with itself in the text
pattern = "Omkar"
text = "my name is Omkar"

match = searchLiteral.searchLiteral(pattern, text)

# 2. Metacharacter
# . -> matches any character except newline
pattern = "a.b"
text1 = "axb"
text2 = "adxb" # more than one char

match = searchLiteral.searchLiteral(pattern, text1)
match = searchLiteral.searchLiteral(pattern, text2)

# * -> matches zero or more characters of preceding charcter
pattern = "ab*"
text1 = "a"
text2 = "ab"
text3 = "abb"

match = searchLiteral.searchLiteral(pattern, text1)
match = searchLiteral.searchLiteral(pattern, text2)
match = searchLiteral.searchLiteral(pattern, text3)

# + -> matches 1 more occurences of preceding character
pattern = "ab+"
text0 = 'a'

match = searchLiteral.searchLiteral(pattern, text0)
match = searchLiteral.searchLiteral(pattern, text1)
match = searchLiteral.searchLiteral(pattern, text2)
match = searchLiteral.searchLiteral(pattern, text3)

# question mark -> matches 0 or 1 occurences of preceding character
