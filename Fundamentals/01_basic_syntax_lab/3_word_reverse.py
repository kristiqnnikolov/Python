# Write a program that receives a single word, reverses it, and prints it.

word = input()
print(word[::-1])

########## ALTERNATIVE SOLUTION ##########


word = input()
result = ""
for char in range(len(word) - 1, -1, -1):
    result += word[char]
print(result)
