# You are going to create a game called "Miner".
# First, you will receive the size of a square field in which the miner should move.
# On the second line, you will receive the commands for the miner's movement, separated by a single space.
# The possible commands are "left", "right", "up" and "down".
# In the end, you will receive each row of the field on a separate line.
# The possible characters that may appear on the screen are:
# •	* - a regular position on the field
# •	e - the end of the route
# •	c - coal
# •	s - miner
# The miner starts moving from the position "s". He should perform the given commands successively,
# moving with only one position in the given direction. If the miner has reached the edge of the field and
# the following command indicates that he has to get out of the area,
# he must remain in his current position and ignore the command.
# When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal.
# In the end, you should print whether the miner has succeeded in collecting the coal or not and his final position:
# •	If the miner has collected all coal in the field, the program stops, and you should print the message:
# "You collected all coal! ({row_index}, {col_index})".
# •	If the miner steps at "e", the game is over (the program stops), and you should print the message:
# "Game over! ({row_index}, {col_index})".
# •	If there are no more commands and none of the above cases had happened, you should print the message:
# "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
# Input
# •	Field size - an integer number
# •	Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
# •	The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
# Output
# •	There are three types of output as mentioned above.

def next_move(command, row, col):  # функция посоки
    if command == 'up':
        return row - 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1
    if command == 'down':
        return row + 1, col


rows = int(input())
commands = input().split()
matrix = []

miner_row = 0
miner_col = 0
all_coals = 0

for row in range(rows):  # пълним матрицата
    symbols = input().split()
    matrix.append(symbols)
    for col in range(rows):  # пълнейки  минаваме през нея
        symbol = symbols[col]
        if symbol == 's':  # намираме s
            miner_row = row  # запаметяваме ред
            miner_col = col  # и колона на миньора
        elif symbol == 'c':  # намираме всички coals
            all_coals += 1

for command in commands:  # минаваме през командите
    next_row, next_col = next_move(command, miner_row, miner_col)  # две променливи за посока и функция

    if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= rows:  # ако посоката е извън матрицата
        continue  # я пропускаме

    miner_row, miner_col = next_row, next_col  # запаметяваме новата позиция на миньора
    if matrix[miner_row][miner_col] == 'c':  # ако миньора е върху coal
        matrix[miner_row][miner_col] = '*'  # заместваме го
        all_coals -= 1  # намаляме общите coals

        if all_coals == 0:  # ако миньора е събрал всички coals
            print(f'You collected all coal! ({miner_row}, {miner_col})')
            exit()
    elif matrix[miner_row][miner_col] == 'e': # ако ексит приключва
        print(f'Game over! ({miner_row}, {miner_col})')
        exit()

print(f'{all_coals} pieces of coal left. ({miner_row}, {miner_col})')
