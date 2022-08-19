# Write a program that returns an encrypted version of the same text.
# Encrypt the text by replacing each character with the corresponding character
# three positions forward in the ASCII table. For example, A would be replaced with D, B would become E, and so on.
# Print the encrypted text.

def ceasar_cipher(text):
    result = ""
    for char in text:
        order = ord(char) + 3
        chrd = chr(order)
        result += chrd
    return result


data = input()
print(ceasar_cipher(data))
