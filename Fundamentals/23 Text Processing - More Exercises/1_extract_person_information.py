# Write a program that reads N lines of strings and extracts the name and the age of a given person:
# •	The person's name will be surrounded by "@" and "|" in the format "@{name}|".
# •	The person's age will be surrounded by "#" and "*" in the format "#{age}*".
# Example: "Hello my name is @Peter| and I am #20* years old."
# For each found name-age pair, print a line in the following format "{name} is {age} years old."

def extract(text):
    name = ""
    age = ""
    text = text.replace("|", " ")
    text = text.replace("*", " ")
    text = text.split()
    for txt in text:
        if "@" in txt:
            for char in range(len(txt)):
                if txt[char] == "@":
                    begin = char + 1
                    name += txt[begin:]
        elif "#" in txt:
            for char in range(len(txt)):
                if txt[char] == "#":
                    begin = char + 1
                    age += txt[begin:]
    print(f'{name} is {age} years old.')


lines = int(input())
for text in range(lines):
    data = input()
    extract(data)
