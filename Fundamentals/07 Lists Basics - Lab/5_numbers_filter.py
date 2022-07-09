# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.


n = int(input())
numbers = []
filtered = []

for i in range(n):
    number = int(input())
    numbers.append(number)
command = input()
if command == "even":
    for num in numbers:
        if num % 2 == 0:
            filtered.append(num)
elif command == "odd":
    for num in numbers:
        if num % 2 != 0:
            filtered.append(num)
elif command == 'negative':
    for num in numbers:
        if num < 0:
            filtered.append(num)
elif command == 'positive':
    for num in numbers:
        if num >= 0:
            filtered.append(num)
print(filtered)
