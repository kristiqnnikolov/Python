# Write a program that reads a string from the console and replaces any sequence
# of the same letters with a single corresponding letter.

def replace(data):
    letter = None
    for char in data:
        if char != letter:
            print(char, end="")
            letter = char


text = input()
replace(text)
