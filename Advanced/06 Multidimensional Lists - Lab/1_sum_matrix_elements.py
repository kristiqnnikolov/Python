# Write a program that reads a matrix from the console and prints:
# •	The sum of all numbers in the matrix
# •	The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated by a comma and a space ", ".

rows, col = [int(x) for x in input().split(', ')]

matrix = []
total = 0

for none in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    total += sum(numbers)
    matrix.append(numbers)

print(total)
print(matrix)
