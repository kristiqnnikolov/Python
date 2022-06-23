# You will be given a string.
# You should print a string in which each character (case-sensitive) is repeated twice.


text = input()
result = ""
for char in text:
    result += char * 2
print(result)
