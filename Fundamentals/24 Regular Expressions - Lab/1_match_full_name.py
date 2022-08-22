# Write a program to match full names from a sequence of characters and print them on the console.

import re
text = input()
matches = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", text)
print(" ".join(matches))
