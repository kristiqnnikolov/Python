# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list.
# You should remove the smallest ones, and then, you should print all the numbers that are left in the list,
# separated by a comma and a space ", ".

numbers = input().split()
remover = int(input())
list = []
for num in numbers:
    list.append(int(num))

for _ in range(remover):
    list.remove(min(list))

result = ', '.join(map(str, list))
print(result)
