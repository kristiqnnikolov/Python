import re

lines = int(input())

for x in range(lines):
    text = input()
    regex = r"(?P<start>.+)>(?P<nums>\d{3})\|(?P<lower>[a-z]{3})\|(?P<upper>[A-Z]{3})\|(?P<symbols>[^>]{3})<(?P<end>\1)"
    matches = re.findall(regex, text)
    result = ""
    if matches:
        for match in matches:
            match = match[1:-1]
            for x in range(len(match)):
                result += match[x]
        print(f"Password: {result}")
    else:
        print("Try another password!")
