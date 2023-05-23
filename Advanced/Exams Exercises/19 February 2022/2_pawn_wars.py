# A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8,
# and columns are marked from A to H. We have a total of 64 squares.
# Each square is represented by a combination of letters and a number (a1, b1, c1, etc.).
# In this problem colors of the board will be ignored.
# We will play the game with two pawns, white (w) and black (b), where they can:
# •	Only move forward in a straight line:
# 	White (w) moves from the 1st rank to the 8th rank direction.
# 	Black (b) moves from 8th rank to the 1st rank direction.
# •	Can move only 1 square at a time.
# •	Can capture another pawn in from of them only diagonally:
# When a pawn reaches the last rank (for the white one - this is the 8th rank,
# and for the black one - this is the 1st rank), can be promoted to a queen.
# Two pawns (w and b) will be placed on two random squares of the bord.
# The first move is always made by the white pawn (w), then black moves (b), then white (w) again, and so on.
#
#
# Some rules apply when moving paws:
# •	If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn.
# When a pawn captures another pawn, the game is over.
# •	If no capture is possible, the pawns keep on moving until one of them reaches the last rank.
# Input
# •	On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
# o	Empty positions are marked with "-".
# o	White pawn is marked with "w"
# o	Black pawn is marked with "b"
# Output
# Print either one of the following:
# •	If a pawn captures the other, print:
# o	"Game over! {White/Black} win, capture on {square}."
# •	If a pawn reaches the last rank, print:
# o	"Game over! {White/Black} pawn is promoted to a queen at {square}."
def attacking(attacker_row, attacker_col, victim_row, victim_col):
    if attacker_row - 1 >= 0 and attacker_col - 1 >= 0:
        if attacker_row - 1 == victim_row and attacker_col - 1 == victim_col:
            return [attacker_row - 1, attacker_col - 1]
    if attacker_row - 1 >= 0 and attacker_col + 1 < 8:
        if attacker_row - 1 == victim_row and attacker_col + 1 == victim_col:
            return [attacker_row - 1, attacker_col + 1]
    if attacker_row + 1 < 8 and col - 1 >= 0:
        if attacker_row + 1 == victim_row and attacker_col - 1 == victim_col:
            return [attacker_row + 1, attacker_col - 1]
    if attacker_row + 1 < 8 and col + 1 < 8:
        if attacker_row + 1 == victim_row and attacker_col + 1 == victim_col:
            return [attacker_row + 1, attacker_col + 1]


white_row = 0
white_col = 0
black_row = 0
black_col = 0
position_row = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1", }
positions_col = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", }
matrix = []
for row in range(8):
    matrix.append(input().split())
    for col in range(8):
        if matrix[row][col] == "w":
            white_row = row
            white_col = col
        if matrix[row][col] == "b":
            black_row = row
            black_col = col

for _ in range(8):
    attack = attacking(white_row, white_col, black_row, black_col)
    if attack:
        position = positions_col[attack[1]] + position_row[attack[0]]
        print(f"Game over! White win, capture on {position}.")
        break

    white_row -= 1
    if white_row == 0:
        position = positions_col[white_col] + position_row[white_row]
        print(f"Game over! White pawn is promoted to a queen at {position}.")
        break

    attack = attacking(black_row, black_col, white_row, white_col)
    if attack:
        position = positions_col[attack[1]] + position_row[attack[0]]
        print(f"Game over! Black win, capture on {position}.")
        break

    black_row += 1
    if black_col == 7:
        position = positions_col[black_col] + position_row[black_row]
        print(f"Game over! Black pawn is promoted to a queen at {position}.")
        break
