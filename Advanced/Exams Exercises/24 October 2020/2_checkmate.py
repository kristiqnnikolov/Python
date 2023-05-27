# You will be given a chess board (8x8). On the board there will be 3 types of symbols:
# •	"." – empty square
# •	"Q" – a queen
# •	"K" – the king
# Your job is to find which queens can capture the king and print them.
# The moves that the queen can do is to move diagonally, horizontally and vertically
# (basically all the moves that all the other figures can do except from the knight).
# Beware that there might be queens that stand in the way of other queens and can stop them from capturing the king.
# For more clarification see the examples.
# Input
# •	8 lines – the state of the board (each square separated by single space)
# Output
# •	The positions of the queens that can capture the king as lists
# •	If the king cannot be captured, print: "The king is safe!"
# •	The order of output does not matter
def queen_movement(q_row, q_col, matrix, rows):
    col = q_col
    for left in range(8):
        col -= 1
        if col < 0:
            break
        if matrix[q_row][col] == 'Q':
            break
        elif matrix[q_row][col] == 'K':
            return [q_row, q_col]
    col = q_col
    for right in range(8):
        col += 1
        if col > 7:
            break
        if matrix[q_row][col] == 'Q':
            break
        elif matrix[q_row][col] == 'K':
            return [q_row, q_col]
    row = q_row
    for up in range(8):
        row -= 1
        if row < 0:
            break
        if matrix[row][q_col] == 'Q':
            break
        elif matrix[row][q_col] == 'K':
            return [q_row, q_col]
    row = q_row
    for down in range(8):
        row += 1
        if row > 7:
            break
        if matrix[row][q_col] == 'Q':
            break
        elif matrix[row][q_col] == 'K':
            return [q_row, q_col]
    col = q_col
    row = q_row
    for left_up_diagonal in range(8):
        row -= 1
        col -= 1
        if row < 0 or col < 0:
            break
        if matrix[row][col] == 'Q':
            break
        elif matrix[row][col] == 'K':
            return [q_row, q_col]
    col = q_col
    row = q_row
    for right_up_diagonal in range(8):
        row -= 1
        col += 1
        if row < 0 or col > 7:
            break
        if matrix[row][col] == 'Q':
            break
        elif matrix[row][col] == 'K':
            return [q_row, q_col]
    col = q_col
    row = q_row
    for left_down_diagonal in range(8):
        row += 1
        col -= 1
        if row > 7 or col < 0:
            break
        if matrix[row][col] == 'Q':
            break
        elif matrix[row][col] == 'K':
            return [q_row, q_col]
    col = q_col
    row = q_row
    for right_down_diagonal in range(8):
        row += 1
        col += 1
        if row > 7 or col > 7:
            break
        if matrix[row][col] == 'Q':
            break
        elif matrix[row][col] == 'K':
            return [q_row, q_col]


rows = 8
matrix = []
king_row = 0
king_col = 0
queens = set()
checkmate_queens = []
for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "K":
            king_row = row
            king_col = col
        elif matrix[row][col] == 'Q':
            queens.add((row, col))

for queen in queens:
    queen_row, queen_col = int(queen[0]), int(queen[1])
    current_queen = queen_movement(queen_row, queen_col, matrix, rows)
    if current_queen:
        checkmate_queens.append(current_queen)
if checkmate_queens:
    for queen in checkmate_queens:
        print(queen)
else:
    print("The king is safe!")