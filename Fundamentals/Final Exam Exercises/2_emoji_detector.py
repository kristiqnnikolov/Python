# Your task is to write a program that extracts emojis from a text and find the threshold based on the input.
# You have to get your cool threshold. It is obtained by multiplying all the digits found in the input.
# The cool threshold could be a huge number, so be mindful.
# An emoji is valid when:
# •	It is surrounded by 2 characters, either "::" or "**"
# •	It is at least 3 characters long (without the surrounding symbols)
# •	It starts with a capital letter
# •	Continues with lowercase letters only
# Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
# Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
# You need to count all valid emojis in the text and calculate their coolness.
# The coolness of the emoji is determined by summing all the ASCII values of all letters in the emoji.
# Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
# You need to print the result of the cool threshold and, after that to take all emojis out of the text,
# count them and print only the cool ones on the console.

import re

text = input()

regex = r"(::|\*\*)([A-Z][a-z]{2,})\1"
matches = re.finditer(regex, text)
cool_meter = 1
result = []
emoji = []
for x in text:
    if x.isdigit():
        cool_meter *= int(x)
for match in matches:
    emoji.append(match[0])
    total = 0
    for i in match[0]:
        if i.isalpha():
            total += ord(i)
        if total >= cool_meter:
            result.append(match)
            break

print(f"Cool threshold: {cool_meter}")
print(f"{len(emoji)} emojis found in the text. The cool ones are:")
for x in result:
    print(x[0])
