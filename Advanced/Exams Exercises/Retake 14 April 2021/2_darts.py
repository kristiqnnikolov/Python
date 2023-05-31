# Two players bare-handedly throw small sharp-pointed missiles known as darts at
# a round target known as a dartboard. Who is going to win this game?
# You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:
# 1	    2	3	4	5	6	7
# 24	D	D	D	D	D	8
# 23	D	T	T	T	D	9
# 22	D	T	B	T	D	10
# 21	D	T	T	T	D	11
# 20	D	D	D	D	D	12
# 19	18	17	16	15	14	13
# Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw for each player.
# The score for each turn is deducted from the player’s total score.
# The first player who reduces their score to zero or less wins the game.
# You are going to receive the information for every throw on a separate line.
# The coordinate information of a hit will be in the format: "({row}, {column})".
# •	If a player hits outside the dartboard, he does not score any points.
# •	If a player hits a number, it is deducted from his total.
# •	If a player hits a "D" the sum of the 4 corresponding numbers per column and row is
# doubled and then deducted from his total.
# •	If a player hits a "T" the sum of the 4 corresponding numbers per column and row is
# tripled and then deducted from his total.
# •	"B" is the bullseye. If a player hits it, he wins the game, and the program ends.
# For example, if Peter hits position with coordinates (2, 1),
# he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are deducted from his total.
# Your job is to find who won the game and with how many turns.
# Input
# •	The name of the first player and the name of the second player, separated by ", "
# •	7 lines – the dartboard (separated by single space)
# •	On the next lines - the coordinates in the format: "({row}, {column})"
# Output
# •	You should print only one line containing the winner and his count of throws:
# "{name} won the game with {count_turns} throws!"
def is_valid(row, col, rows):
    return rows > row >= 0 and 0 <= col < rows


def game_over(points, player, turns):
    if points <= 0:
        print(f"{player} won the game with {turns} throws!")
        exit()


def points(player, matrix, row, col, player_turns):
    player_points = 0
    total = int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])
    if matrix[row][col] == 'B':
        game_over(0, player, player_turns)
    elif matrix[row][col] == 'D':
        player_points += total * 2
    elif matrix[row][col] == 'T':
        player_points += total * 3
    else:
        player_points += int(matrix[row][col])
    return player_points


player_1, player_2 = input().split(', ')

player_1_points = 501
player_2_points = 501
player_1_turns = 0
player_2_turns = 0
rows = 7
matrix = []
for x in range(rows):
    matrix.append([x for x in input().split()])

while True:
    left_strip = input().strip('(')
    right_strip = left_strip.strip(')')
    row, col = right_strip.split(', ')
    row = int(row)
    col = int(col)
    player_1_turns += 1
    if is_valid(row, col, rows):
        player_1_points -= points(player_1, matrix, row, col, player_1_turns)
        game_over(player_1_points, player_1, player_1_turns)
    left_strip = input().strip('(')
    right_strip = left_strip.strip(')')
    row, col = right_strip.split(', ')
    row = int(row)
    col = int(col)
    player_2_turns += 1
    if is_valid(row, col, rows):
        player_2_points -= points(player_2, matrix, row, col, player_2_turns)
        game_over(player_2_points, player_2, player_2_turns)
