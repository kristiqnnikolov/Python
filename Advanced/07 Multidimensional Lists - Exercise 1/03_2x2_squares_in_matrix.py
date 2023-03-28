# Find the number of all 2x2 squares containing identical chars in a matrix.
# On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}".
# On the following rows, you will receive characters separated by a single space.
# Print the number of all square matrices you have found.
def the_matrix(rows):
    matrix = []
    for none in range(rows):
        matrix.append([x for x in input().split()])
    return matrix


rows, cols = [int(x) for x in input().split()]
matrix = the_matrix(rows)
matches = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        square_matrix = [matrix[row][col], matrix[row][col + 1],
                         matrix[row + 1][col], matrix[row + 1][col + 1]]
        if square_matrix[0] == square_matrix[1] == \
                square_matrix[2] == square_matrix[3]:
            matches += 1
print(matches)
