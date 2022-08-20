# Write a program that prints the sum of all found characters between two given characters (their ASCII code).
# On each of the first two lines, you will receive a single character. On the last line, you get a random string.
# Print the sum of the ASCII values of all characters in the random string between
# the two given characters in the ASCII table.

def ascii_sumator(symbol_1, symbol_2, data):
    total = 0
    for x in data:
        if symbol_1 < ord(x) < symbol_2:
            total += ord(x)
    print(total)


symbol1 = ord(input())
symbol2 = ord(input())
text = input()
ascii_sumator(symbol1, symbol2, text)
