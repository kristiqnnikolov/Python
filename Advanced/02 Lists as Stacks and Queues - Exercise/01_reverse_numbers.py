# Write a program which reads from the console a string with N integers, separated by a single space, and
# reverses them using a stack. Print the reversed integers on one line, separated by a single space.
text = input().split()
reversed = []

for x in range(len(text)):
    reversed.append(int(text.pop()))
print(*reversed, sep=" ")
