# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right).
# On the first line, you will receive an integer N – the size of a square matrix.
# The next N lines holds the values for each column - N numbers, separated by a single space.

lines = int(input())

matrix = []
total = 0
for none in range(lines):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

for i in range(lines):
    total += matrix[i][i]

print(total)
