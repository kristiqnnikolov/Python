# Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy".
# Use capturing groups in your regular expression.

import re

text = input()
regex = "(?P<Day>\d{2})(?P<separator>[\.\-\/])(?P<Month>[A-Z][a-z]+)(?P=separator)(?P<Year>[0-9]{4})"
matches = re.finditer(regex, text)
group = [match.groupdict() for match in matches]
for key in group:
    print(f'Day: {key["Day"]}, Month: {key["Month"]}, Year: {key["Year"]}')
