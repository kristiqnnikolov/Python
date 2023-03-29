# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of
# its elements. There will be no case with two or more 3x3 squares with equal maximal sum.
# Input
# •	On the first line, you will receive the rows and columns in the format "{rows} {columns}" –
# integers in the range [1, 20]
# •	On the following lines, you will receive each row with its columns -
# integers, separated by a single space in the range [-20, 20]
# Output
# •	On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
# •	On the following 3 lines, print each element of the found submatrix, separated by a single space
def the_matrix(rows):
    matrix = []
    for none in range(rows):
        matrix.append([int(x) for x in input().split()])
    return matrix


rows, cols = [int(x) for x in input().split()]
matrix = the_matrix(rows)
max = -9
max_matrix = []


for row in range(rows-2):
    for col in range(cols-2):
        square_matrix = [matrix[row][col], matrix[row][col+1], matrix[row][col+2],
                         matrix[row+1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2],
                         matrix[row+2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        if sum(square_matrix) > max:
            max = sum(square_matrix)
            max_matrix = square_matrix
print(f"Sum = {max}")
print(f'{max_matrix[0]} {max_matrix[1]} {max_matrix[2]}')
print(f'{max_matrix[3]} {max_matrix[4]} {max_matrix[5]}')
print(f'{max_matrix[6]} {max_matrix[7]} {max_matrix[8]}')
