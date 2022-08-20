# Write a program that decrypts a message by a given key and gathers information about hidden treasure type and
# its coordinates. On the first line, you will receive a key (sequence of numbers separated by a space).
# On the next few lines, you will receive lines with strings until you get the command "find".
# You should loop through every string and decrease the ASCII code of each character with a corresponding number of the
# key sequence. You choose a key number from the sequence by just looping through it.
# If the length of the key sequence is less than the string sequence, you should continue looping from the beginning.
# For more clarification, see the example below.
# After decrypting the message, you will get a type of treasure and its coordinates.
# The type will be between the symbol "&", and the coordinates - between the symbols "<' and '>'.
# For each line print the type and the coordinates in the format "Found {type} at {coordinates}".

import re

index = [x for x in input().split()]
index = "".join(index)

text = input()
while not text == 'find':
    while len(text) > len(index):
        index *= 2
    message = ''

    for x in range(len(text)):
        letter = ord(text[x]) - int(index[x])
        message += chr(letter)
    regex_material = r"&(\w+)&"
    regex_coordinates = r"<(\w+)>"
    material = re.findall(regex_material, message)
    coordinates = re.findall(regex_coordinates, message)
    print(f'Found {material[0]} at {coordinates[0]}')
    text = input()
