# On the first line you will receive a string. On the second line you will receive a second string.
# Write a program which removes all the occurrences of the first string in the second until there is no match.
# At the end print the remaining string.

text = input()
string = input()
while text in string:
    string = string.replace(text, "")
print(string)
