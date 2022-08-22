# Write a regular expression to match a valid phone number from Sofia.
# After you find all valid phones, print them on the console, separated by a comma and a space ", ".

import re

text = input()
matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", text)
result = []
for match in matches:
    result.append(match.group())
print(", ".join(result))
