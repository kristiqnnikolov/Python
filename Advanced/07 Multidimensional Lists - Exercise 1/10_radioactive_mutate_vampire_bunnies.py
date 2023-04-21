# You come across an old JS Basics teamwork game. It is about bunnies that multiply extremely fast.
# There's also a player that should escape from their lair.
# You like the game, so you decide to port it to Python because that's your language of choice.
# The last thing left is the algorithm that determines if the player will escape the lair or not.
# First, you will receive a line holding integers N and M, representing the lair's rows and columns.
# Next, you receive N strings that can consist only of ".", "B", "P". They represent the initial state of the lair.
# There will be only one player. The bunnies are marked with "B", the player is marked with "P", and
# everything else is free space, marked with a dot ".".
# Then you will receive a string with commands (e.g., LRRULUD) - each letter represents the next move of the player:
# •	L - the player should move one position to the left
# •	R - the player should move one position to the right
# •	U - the player should move one position up
# •	D - the player should move one position down
# After every step made, each bunny spreads one position up, down, left, and right.
# If the player moves to a bunny cell or a bunny reaches the player, the player dies.
# If the player goes out of the lair without encountering a bunny, the player wins.
# When the player dies or wins, the game ends. All the activities for this turn continue
# (e.g., all the bunnies spread normally), but there are no more turns.
# There will be no cases where the moves of the player end before he dies or escapes.
# In the end, print the final state of the lair with every row on a separate line. On the last line,
# print either "dead: {row} {col}" or "won: {row} {col}". "Row" and "col" are the cell coordinates where
# the player has died or the last cell he has been in before escaping the lair.

def next_move(row, col, command):
    if command == 'U':
        return row - 1, col
    if command == 'L':
        return row, col - 1
    if command == 'R':
        return row, col + 1
    if command == 'D':
        return row + 1, col


def invalid(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(x) for x in input().split()]

matrix = []
player_row = 0
player_col = 0
bunnies = set()

for row in range(rows):
    row_elements = list(input())
    matrix.append(row_elements)

    for col in range(cols):
        if row_elements[col] == 'P':
            player_row = row
            player_col = col
        elif row_elements[col] == 'B':
            bunnies.add(f'{row} {col}')

won = False
dead = False

commands = input()

matrix[player_row][player_col] = '.'

for command in commands:
    next_row, next_col = next_move(player_row, player_col, command)

    if invalid(next_row, next_col, rows, cols):
        won = True
    elif matrix[next_row][next_col] == 'B':
        dead = True
        player_row, player_col = next_row, next_col
    else:
        player_row, player_col = next_row, next_col

    new_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]

        if not invalid(bunny_row - 1, bunny_col, rows, cols):
            new_bunnies.add(f'{bunny_row - 1} {bunny_col}')
            matrix[bunny_row - 1][bunny_col] = 'B'
        if not invalid(bunny_row + 1, bunny_col, rows, cols):
            new_bunnies.add(f'{bunny_row + 1} {bunny_col}')
            matrix[bunny_row + 1][bunny_col] = 'B'
        if not invalid(bunny_row, bunny_col - 1, rows, cols):
            new_bunnies.add(f'{bunny_row} {bunny_col - 1}')
            matrix[bunny_row][bunny_col - 1] = 'B'
        if not invalid(bunny_row, bunny_col + 1, rows, cols):
            new_bunnies.add(f'{bunny_row} {bunny_col + 1}')
            matrix[bunny_row][bunny_col + 1] = 'B'

    bunnies = bunnies.union(new_bunnies)

    if matrix[player_row][player_col] == 'B':
        dead = True

    if won or dead:
        break

for row in matrix:
    print(*row, sep='')

if won:
    print(f'won: {player_row} {player_col}')
else:
    print(f'dead: {player_row} {player_col}')