# Write a program that reads a text from the console and counts the occurrences of each character in it.
# Print the results in alphabetical (lexicographical) order.

text = input()

symbols = {}

for x in text:
    if x not in symbols:
        symbols[x] = 0
    symbols[x] += 1
for symbol, times in sorted(symbols.items()):
    print(f'{symbol}: {times} time/s')
