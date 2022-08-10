# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

data = input()
dictionary = {}
for letter in data:
    if letter != ' ':
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1
for key, value in dictionary.items():
    print(f'{key} -> {value}')
