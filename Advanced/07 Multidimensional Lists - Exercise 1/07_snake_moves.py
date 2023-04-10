# You are tasked to visualize a snake's zigzag path in a rectangular matrix with a size N x M.
# A string represents the snake. It starts moving from the top-left corner to the right.
# When the snake reaches the end of the row, it slithers its way down to the next row and turns left.
# The moves are repeated to the very end.
# The first cell is filled with the first symbol of the snake. The second cell is filled with the second symbol, etc.
# The snake's path is as long as it takes to fill the matrix completely -
# if you reach the end of the string representing the snake, start again at the first symbol.
# In the end, you should print the snake's path.
# Input
# The input data consists of exactly two lines:
# •	On the first line, you will receive the dimensions N x M of the field in format: "{rows} {columns}".
# •	On the second line, you will receive the string representing the snake
# Output
# •	You should print the snake's zigzag path of size N x M (rows x columns)
def the_matrix(row, col):
    matrix = []
    for none in range(row):
        matrix.append(["x" for x in range(col)])
    return matrix


rows, cols = [int(x) for x in input().split()]
word = input()
matrix = the_matrix(rows, cols)

word_index = 0

for row_index in range(rows):
    for col_index in range(cols):
        matrix[row_index][col_index] = word[word_index]
        word_index += 1
        if word_index == len(word):
            word_index = 0

for row_index in range(rows):
    if row_index % 2 == 1:
        matrix[row_index] = matrix[row_index][::-1]
    print(''.join(matrix[row_index]))
