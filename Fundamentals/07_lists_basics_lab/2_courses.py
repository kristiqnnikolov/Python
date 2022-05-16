# On the first line, you will receive a single number n.
# On the following n lines, you will receive names of courses. You should create a list of courses and print it.

n = int(input())
list = []
for i in range(n):
    command = input()
    list.append(command)
print(list)
