# On the first line, you will receive a number n. On the second line, you will receive a word.
# On the following n lines, you will be given some strings. You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.


n = int(input())
word = input()
list = []

for i in range(n):
    text = input()
    list.append(text)
print(list)
for z in range(len(list) - 1, -1, -1):
    element = list[z]
    if word not in element:
        list.remove(element)
print(list)
