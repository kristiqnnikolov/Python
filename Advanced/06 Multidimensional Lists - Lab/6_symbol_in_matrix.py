# Write a program that reads a number - N, representing the rows and columns of a square matrix.
# On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters.
# After that, you will receive a symbol.
# Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})".
# You should start searching from the top left.
# If there is no such symbol print the message "{symbol} does not occur in the matrix".

lines = int(input())
matrix = [list(input()) for none in range(lines)]
symbol = input()
is_found = False

for row in range(lines):
    for col in range(lines):
        if symbol == matrix[row][col]:
            is_found = True
            print((row, col))
            break
    if is_found:
        break
if not is_found:
    print(f'{symbol} does not occur in the matrix')
