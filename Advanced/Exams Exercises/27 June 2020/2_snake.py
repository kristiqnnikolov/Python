# Everybody remembers the old snake game. Now it is time to create your own.
#
# You will be given an integer n for the size of the snake territory with square shape.
# On the next n lines, you will receive the rows of the territory.
# The snake will be placed on a random position, marked with the letter 'S'.
# On random positions there will be food, marked with '*'. There might also be a lair on the territory.
# The lair has two burrows. They are marked with the letter - 'B'. All of the empty positions will be marked with '-'.
# Each turn, you will be given command for the snake’s movement. When the snake moves it leaves a trail marked with '.'
# Move commands will be: "up", "down", "left", "right".
# If the snake moves to a food, it eats the food and increases the food quantity with one.
# If it goes inside of a burrow, it goes out on the position of the other burrow and then both burrows disappear.
# If the snake goes out of its territory, it loses, can't return back and the program ends.
# The snake needs at least 10 food quantity to win.
# When the snake has gone outside of its territory or has eaten enough food, the game ends.
# Input
# •	On the first line, you are given the integer n – the size of the square matrix.
# •	The next n lines holds the values for every row.
# •	On each of the next lines you will get a move command.
# Output
# •	On the first line:
# o	If the snake goes out of its territory, print: "Game over!"
# o	If the snake eat enough food, print: "You won! You fed the snake."
# •	On the second line print all food eaten: "Food eaten: {food quantity}"
# •	In the end print the matrix.
def is_valid(row, col, rows):
    return 0 <= row < rows and 0 <= col < rows


def next_move(command, row, col):
    if command == 'up':
        return row - 1, col
    elif command == 'left':
        return row, col - 1
    elif command == 'right':
        return row, col + 1
    elif command == 'down':
        return row + 1, col


rows = int(input())
matrix = []
snake_row = 0
snake_col = 0
burrow = []
food = 0

for row in range(rows):
    matrix.append([x for x in input()])
    for col in range(rows):
        if matrix[row][col] == 'S':
            snake_row = row
            snake_col = col
        elif matrix[row][col] == 'B':
            burrow.append([row, col])

while True:
    command = input()
    next_row, next_col = next_move(command, snake_row, snake_col)
    if not is_valid(next_row, next_col, rows):
        matrix[snake_row][snake_col] = '.'
        print("Game over!")
        break
    if matrix[next_row][next_col] == '*':
        food += 1
        matrix[snake_row][snake_col] = '.'
        matrix[next_row][next_col] = 'S'
        snake_row, snake_col = next_row, next_col
        if food == 10:
            print("You won! You fed the snake.")
            break
    elif matrix[next_row][next_col] == 'B':
        if [next_row, next_col] == burrow[0]:
            matrix[burrow[0][0]][burrow[0][1]] = '.'
            matrix[snake_row][snake_col] = '.'
            snake_row, snake_col = burrow[1][0], burrow[1][1]
            matrix[snake_row][snake_col] = 'S'
        elif [next_row, next_col] == burrow[1]:
            matrix[burrow[1][0]][burrow[1][1]] = '.'
            matrix[snake_row][snake_col] = '.'
            snake_row, snake_col = burrow[0][0], burrow[0][1]
            matrix[snake_row][snake_col] = 'S'
        del burrow
    else:
        matrix[snake_row][snake_col] = '.'
        matrix[next_row][next_col] = 'S'
        snake_row, snake_col = next_row, next_col

print(f"Food eaten: {food}")
for row in matrix:
    print(*row, sep='')