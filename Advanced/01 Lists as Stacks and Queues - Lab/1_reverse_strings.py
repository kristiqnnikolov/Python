# Write program that:
# •	Reads an input string
# •	Reverses it using a stack
# •	Prints the result back on the console

text = list(input())
reversed = []

for i in range(len(text)):
    reversed.append(text.pop())
print("".join(reversed))
