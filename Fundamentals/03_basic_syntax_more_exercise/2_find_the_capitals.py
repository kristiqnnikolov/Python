# Write a program that takes a single string and prints a list of all the capital letters indices.

text = input()
result = []
for index in range(len(text)):
    if text[index].isupper():
        result.append(index)
print(result)
