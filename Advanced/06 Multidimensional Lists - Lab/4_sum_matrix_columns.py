# Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
# On the first line, you will get matrix sizes in format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated with a single space.

rows, cols = [int(x) for x in input().split(', ')]
matrix = []
for none in range(rows):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)
for col in range(cols):
    result = 0
    for row in range(rows):
        result += matrix[row][col]
    print(result)
