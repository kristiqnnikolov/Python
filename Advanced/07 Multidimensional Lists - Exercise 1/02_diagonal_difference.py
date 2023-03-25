# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
# On the first line, you will receive an integer N - the size of a square matrix.
# The following N lines hold the values for each column - N numbers separated by a single space.
# Print the absolute difference between the primary and the secondary diagonal sums.

def the_matrix(rows):
    matrix = []
    for none in range(rows):
        matrix.append([int(x) for x in input().split()])
    return matrix


lines = int(input())
matrix = the_matrix(lines)

primary = 0
secondary = 0

for row in range(lines):
    for col in range(lines - 1, -1, -1):
        if row + col == lines - 1:
            secondary += matrix[row][col]
        if row == col:
            primary += matrix[row][col]

difference = abs(primary - secondary)
print(difference)
