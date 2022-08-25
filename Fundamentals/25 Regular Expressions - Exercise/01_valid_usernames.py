# Write a program that reads usernames on a single line (separated by ", ") and prints
# all valid usernames on separate lines.
# A valid username:
# •	has length between 3 and 16 characters inclusive
# •	can contain only letters, numbers, hyphens, and underscores
# •	has no redundant symbols before, after, or in between

def valid(data):
    for text in data:
        if 3 <= len(text) <= 16:
            for char in range(len(text)):
                if text[char].isalpha() or text[char].isdigit() or text[char] == "-" or text[char] == "_":
                    if char == len(text) - 1:
                        print(text)
                else:
                    break


data = input().split(", ")
valid(data)
