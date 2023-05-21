# You are playing a game, and your goal is to collect 100 coins.
# On the first line, you will be given a number representing the size of the field with a square shape. On the following few lines, you will be given the field with:
# •	One player - randomly placed in it and marked with the symbol "P"
# •	Numbers for coins placed at different positions of the field
# •	Walls marked with "X"
# After the field state, you will be given commands for the player's movement.
# Commands can be: "up", "down", "left", "right". If the command is invalid, you should ignore it.
# The player moves in the given direction with one step for each command and collects all the coins that come across.
# If he goes out of the field, he should continue to traverse the field from the opposite side in the same direction.
# Note: He can go through the same path many times, but he can collect the coins just once (the first time).
# There are only two possible outcomes of the game:
# •	The player hits a wall, loses the game, and his coins are reduced to 50% and rounded down to the next-lowest number.
# •	The player collects at least 100 coins and wins the game.
# For more clarifications, see the examples below.
# Input
# •	A number representing the size of the field (matrix NxN)
# •	A matrix representing the field (each position separated by a single space)
# •	On each of the following lines, you will get a move command.
# Output
# •	If the player won the game, print: "You won! You've collected {total_coins} coins."
# •	If the player loses the game, print: "Game over! You've collected {total_coins} coins."
# •	Collected coins have to be rounded down to the next-lowest number.
# •	The player's path as cooridnates in lists on separate lines:
# "Your path:
# [{row_position1}, {column_position1}]
# [{row_position2}, {column_position2}]
# …
# [{row_positionN}, {column_positionN}]"
def next_move(command, row, col):
    if command == 'up':
        if row - 1 < 0:
            return rows - 1, col
        else:
            return row - 1, col
    if command == 'left':
        if col - 1 < 0:
            return row, rows - 1
        else:
            return row, col - 1
    if command == 'right':
        if col + 1 > rows - 1:
            return row, 0
        else:
            return row, col + 1
    if command == 'down':
        if row + 1 > rows - 1:
            return 0, col
        else:
            return row + 1, col


rows = int(input())
matrix = []
player_row = 0
player_col = 0
coins = 0
path = ""
for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == 'P':
            player_row = row
            player_col = col
            path += f"{[player_row, player_col]}\n"

while True:
    command = input()
    next_row, next_col = next_move(command, player_row, player_col)
    if matrix[next_row][next_col] == 'X':
        coins = coins // 2
        path += f"{[next_row, next_col]}\n"
        print(f"Game over! You've collected {coins} coins.")
        break
    coins += int(matrix[next_row][next_col])
    path += f"{[next_row, next_col]}\n"
    matrix[player_row][player_col] = 0
    player_row, player_col = next_row, next_col
    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

print("Your path:")
print(path)
