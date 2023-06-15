# You will be given an integer n for the size of the mines field with square shape and another one for the number of
# bombs that you have to place in the field. On the next n lines, you will receive the position for each bomb.
# Your task is to create the game field placing the bombs at the correct positions and mark them with "*",
# and calculate the numbers in each cell of the field. Each cell represents a number of all bombs directly near it
# (up, down, left, right and the 4 diagonals).
# Input
# •	On the first line, you are given the integer n – the size of the square matrix.
# •	On the second line – the number of the bombs.
# •	The next n lines holds the position of each bomb.
# Output
# •	Print the matrix you've created.
def is_inside(row, col, rows):
    return 0 <= row < rows and 0 <= col < rows


def adding(row, col, rows, matrix):
    if is_inside(row, col, rows):
        if matrix[row][col] == "*":
            return 1
    return 0


def bombs(row, col, matrix):
    number = adding(row - 1, col, rows, matrix) + adding(row - 1, col - 1, rows, matrix) + \
             adding(row - 1, col + 1, rows, matrix) + adding(row + 1, col + 1, rows, matrix) + \
             adding(row, col - 1, rows, matrix) + adding(row, col + 1, rows, matrix) + \
             adding(row + 1, col, rows, matrix) + adding(row + 1, col - 1, rows, matrix)
    return number


rows = int(input())
number_of_bombs = int(input())

matrix = []
for row in range(rows):
    line = []
    for x in range(rows):
        line.append("0")
    matrix.append(line)

for none in range(number_of_bombs):
    [row, col] = map(lambda x: int(x), input()[1:][:-1].split(', '))
    matrix[row][col] = '*'

for row in range(rows):
    for col in range(rows):
        if not matrix[row][col] == '*':
            number = bombs(row, col, matrix)
            matrix[row][col] = number

for row in matrix:
    print(*row)
