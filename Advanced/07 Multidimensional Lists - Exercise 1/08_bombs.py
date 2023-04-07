# You will be given a square matrix of integers, each integer separated by a single space,
# and each row will be on a new line. On the last line of input, you will receive indexes -
# coordinates of several cells separated by a single space, in the following format:
# "{row1},{column1} {row2},{column2} … {row3},{column3}".
# On those cells, there are bombs. You must detonate every bomb in the order they were given.
# When a bomb explodes, it deals damage equal to its integer value to all the cells around it
# (in every direction and in all diagonals). One bomb can't explode more than once, and after it does,
# its value becomes 0. When a cell's value reaches 0 or below, it dies. Dead cells can't explode.
# You must print the count of all alive cells and their sum.
# Afterward, print the matrix with all its cells (including the dead ones).
# Input
# •	On the first line, you are given the integer N - the size of the square matrix.
# •	The following N lines hold each column's values - N numbers separated by a space.
# •	On the last line, you will receive the coordinates of the cells with the bombs in the format described above.
# Output
# •	On the first line, you need to print the count of all alive cells in the format:
# "Alive cells: {alive_cells}"
# •	On the second line, you need to print the sum of all alive cells in the format:
# "Sum: {sum_of_cells}"
# •	In the end, print the matrix. A space must separate the cells.

def the_matrix(rows):
    matrix = []
    for none in range(rows):
        matrix.append([int(x) for x in input().split()])
    return matrix


rows = int(input())
matrix = the_matrix(rows)
all_coordinates = input().split()
for bombs_coord in all_coordinates:
    coordinates = bombs_coord.split(",")
    bomb_row = int(coordinates[0])
    bomb_col = int(coordinates[1])
    if matrix[bomb_row][bomb_col] <= 0:
        continue
    bomb_power = matrix[bomb_row][bomb_col]
    matrix[bomb_row][bomb_col] = 0

    for i in range(bomb_row - 1, bomb_row + 2):
        for j in range(bomb_col - 1, bomb_col + 2):
            if 0 <= i < rows and 0 <= j < rows and matrix[i][j] > 0:
                matrix[i][j] -= bomb_power

alive_cells = 0
alive_cells_sum = 0
for row in matrix:
    for x in row:
        if x > 0:
            alive_cells += 1
            alive_cells_sum += x

print(f'Alive cells: {alive_cells}')
print(f'Sum: {alive_cells_sum}')
for row in matrix:
    print(*row, sep=' ')
