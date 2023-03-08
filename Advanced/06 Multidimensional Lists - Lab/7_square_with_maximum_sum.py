# Write a program that reads a matrix from the console and finds the 2x2 top-left
# submatrix with biggest sum of its values.
# On first line you will get matrix sizes in format "{rows}, {columns}".
# On the next rows, you will get elements for each column, separated with a comma and a space ", ".
# You should print the found submatrix and the sum of its elements as shown in the examples.

rows, cols = [int(x) for x in input().split(", ")]
matrix = []

max = -9
max_matrix = []
for none in range(rows):
    numbers = [int(x) for x in input().split(', ')]
    matrix.append(numbers)

for row in range(rows - 1):
    for col in range(cols - 1):
        square_matrix = [matrix[row][col], matrix[row][col + 1],
                         matrix[row + 1][col], matrix[row + 1][col + 1]]
        total = sum(square_matrix)
        if total > max:
            max = total
            max_matrix = square_matrix.copy()
print(max_matrix[0], max_matrix[1])
print(max_matrix[2], max_matrix[3])
print(max)
