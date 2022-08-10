# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and print its details in the format:
# "{name} -> {number}". In case the contact isn't found, print: "Contact {name} does not exist."

dictionary = {}
while True:
    entry = input().split('-')
    if not entry[0].isdigit():
        names = entry[0]
        phone_number = entry[1]
        if names not in dictionary:
            dictionary[names] = phone_number
        else:
            dictionary[names] = phone_number
    else:
        break
for count in range(1, int(entry[0]) + 1):
    name = input()
    if name in dictionary:
        print(f'{name} -> {dictionary[name]}')
    else:
        print(f'Contact {name} does not exist.')
