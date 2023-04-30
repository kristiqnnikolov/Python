# The presents are ready, and Santa has to deliver them to the kids.
# You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood
# with a square shape. On the following lines, you will receive the matrix, which represents the neighborhood.
# Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live.
# If the cell has "X" on it, that means there lives a naughty kid. Otherwise,
# if a nice kid lives there, the cell is marked by "V". There can also be cells marked with "C" for cookies.
# All of the empty positions will be marked with "-".
# Santa can move "up", "down", "left", "right" with one position each time. These will be the commands that you receive.
# If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a house with a naughty kid,
# he doesn't drop a present. If the command sends Santa to a cell marked with "C",
# Santa eats cookies and becomes happy and extra generous to all the kids around him*
# (meaning all of them will receive presents - it doesn't matter if naughty or nice).
# If Santa has been to a house, the cell becomes "-".
# Note: *around him means on his left, right, upwards, and downwards by one cell.
# In this case, Santa doesn't move to these cells, or if he does, he returns to the cell where the cookie was.
# If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
# Keep in mind that you should check whether all the nice kids received presents.
# Input
# •	On the first line, you are given the integer m - the count of presents
# •	On the second - integer n - the size of the neighborhood
# •	The following n lines hold the values for every row
# •	On each of the following lines you will get a command
# Output
# •	On the first line:
# o	If Santa runs out of presents, but there are still some nice kids left print: "Santa ran out of presents!"
# •	Next, print the matrix.
# •	In the end, print one of these messages:
# o	If he manages to give all the nice kids presents, print:
# "Good job, Santa! {count_nice_kids} happy nice kid/s."
# o	Otherwise, print:
# "No presents for {count nice kids} nice kid/s."
def next_move(command, row, col):  # функция посоки
    if command == 'up':
        return row - 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1
    if command == 'down':
        return row + 1, col


def happy(matrix, row, col, presents, nice_kids, nice_kids_with_presents):
    return matrix[row][col] == '-', presents - 1, nice_kids - 1, nice_kids_with_presents + 1


presents = int(input())
rows = int(input())
matrix = []
santa_row = 0
santa_col = 0
no_presents = False
nice_kids = 0
nice_kids_with_presents = 0

for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "S":
            santa_row = row
            santa_col = col
        elif matrix[row][col] == 'V':
            nice_kids += 1

while True:
    command = input()
    if command == 'Christmas morning':
        break

    next_row, next_col = next_move(command, santa_row, santa_col)
    if matrix[next_row][next_col] == 'C':
        matrix[santa_row][santa_col] = '-'
        matrix[next_row][next_col] = 'S'
        if matrix[next_row - 1][next_col] == 'V':
            happy(matrix, next_row - 1, next_col, presents, nice_kids, nice_kids_with_presents)
        elif matrix[next_row - 1][next_col] == 'X':
            matrix[next_row - 1][next_col] = '-'
            presents -= 1
        if matrix[next_row][next_col - 1] == 'V':
            happy(matrix, next_row, next_col - 1, presents, nice_kids, nice_kids_with_presents)
        elif matrix[next_row][next_col - 1] == 'X':
            matrix[next_row][next_col - 1] = '-'
            presents -= 1
        if matrix[next_row][next_col + 1] == 'V':
            matrix[next_row][next_col + 1] = '-'
            presents -= 1
            nice_kids -= 1
            nice_kids_with_presents += 1
        elif matrix[next_row][next_col + 1] == 'X':
            matrix[next_row][next_col + 1] = '-'
            presents -= 1
        if matrix[next_row + 1][next_col] == 'V':
            matrix[next_row + 1][next_col] = '-'
            presents -= 1
            nice_kids -= 1
            nice_kids_with_presents += 1
        elif matrix[next_row + 1][next_col] == 'X':
            matrix[next_row + 1][next_col] = '-'
            presents -= 1
    elif matrix[next_row][next_col] == 'V':
        matrix[santa_row][santa_col] = '-'
        presents -= 1
        nice_kids -= 1
        nice_kids_with_presents += 1
        matrix[next_row][next_col] = 'S'
        santa_row, santa_col = next_row, next_col
    elif matrix[next_row][next_col] == 'X':
        matrix[santa_row][santa_col] = '-'
        matrix[next_row][next_col] = 'S'
        santa_row, santa_col = next_row, next_col
    else:
        matrix[santa_row][santa_col] = '-'
        santa_row, santa_col = next_row, next_col
    if presents == 0:
        no_presents = True
        break
if no_presents and nice_kids:
    print(f"Santa ran out of presents!")
for row in matrix:
    print(*row, sep=' ')
if not nice_kids:
    print(f"Good job, Santa! {nice_kids_with_presents} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
