# Write a program which receives a single string.
# On the first line it should print all the digits found in the string, on the second – all the letters, and
# on the third – all the other characters. There will always be at least one digit, one letter and one other characters.

text = input()
numbers = ""
letters = ""
symbols = ""
for char in text:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        symbols += char
print(numbers)
print(letters)
print(symbols)
