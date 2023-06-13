# You will be given a string. Then, you will be given an integer N for the size of the field with square shape.
# On the next N lines, you will receive the rows of the field. The player will be placed on a random position,
# marked with "P". On random positions there will be letters. All of the empty positions will be marked with "-".
# Each turn you will be given commands for the player’s movement.
# If he moves to a letter, he consumes it, concatеnates it to the initial string and
# the letter disappears from the field. If he tries to move outside of the field,
# he is punished - he loses the last letter in the string, if there are any, and the player’s position is not changed.
# At the end print all letters and the field.
# Input
# •	On the first line, you are given the initial string
# •	On the second line, you are given the integer N - the size of the square matrix
# •	The next N lines holds the values for every row
# •	On the next line you receive a number M
# •	On the next M lines you will get a move command
# Output
# •	On the first line the final state of the string
# •	In the end print the matrix
def next_move(row, col, command):
    if command == 'up':
        return row - 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1
    if command == 'down':
        return row + 1, col


def is_valid(row, col, rows):
    return 0 <= row < rows and 0 <= col < rows


word = input()
rows = int(input())

matrix = []
player_row = 0
player_col = 0

for row in range(rows):
    matrix.append([x for x in input()])
    for col in range(rows):
        if matrix[row][col] == 'P':
            player_row = row
            player_col = col

number_of_commands = int(input())
for none in range(number_of_commands):
    command = input()
    next_row, next_col = next_move(player_row, player_col, command)
    if is_valid(next_row, next_col, rows):
        if not matrix[next_row][next_col] == '-':
            word += str(matrix[next_row][next_col])
        matrix[next_row][next_col] = 'P'
        matrix[player_row][player_col] = '-'
        player_row, player_col = next_row, next_col
    else:
        if len(word) > 0:
            word = word[:-1]

print(word)
for row in matrix:
    print(*row, sep='')
