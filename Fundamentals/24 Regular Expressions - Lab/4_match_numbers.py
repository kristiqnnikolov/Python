# Write a program that finds all integer and floating-point numbers in a string.

import re

text = input()
regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"
matches = re.finditer(regex, text)
result = []
for match in matches:
    result.append(match.group())
print(" ".join(result))
