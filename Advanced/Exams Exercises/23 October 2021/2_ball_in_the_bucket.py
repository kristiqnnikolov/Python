# You are at the funfair to play different games and test your skills. Now you are playing ball in the bucket game.
# You will be given a matrix with 6 rows and 6 columns representing the board. On the board, there will be points
# (integers) and buckets marked with the letter "B". Rules of the game:
# •	You can throw a ball only 3 times.
# •	When you hit a bucket (position marked with 'B'), you score the sum of the points in the same column.
# •	You can hit a bucket only once. If you hit the same bucket again, you do not score any points.
# •	If you hit outside a bucket (hit a number on the board) or outside the board, you do not score any points.
# After the board state, you are going to receive the information for every throw on a separate line.
# The coordinates’ information of a hit will be in the format: "({row}, {column})".
# Depending on how many points you have collected, you win one of the following:
# Football	100 to 199 points
# Teddy Bear	200 to 299 points
# Lego Construction Set	300 and more points
#
# Your job is to keep track of the scored points and to check if you won a prize.
# For more clarifications, see the examples below.
# Input
# •	6 lines – matrix representing the board (each position separated by a single space)
# •	On the next 3 lines - the coordinates of the throw in the format: "({row}, {column})"
#
# Output
# •	On the first line:
# o	If you won a prize, print:
# "Good job! You scored {points} points, and you've won {prize}."
# o	If you did not win any prize, print the points you need to get at least the first prize:
# "Sorry! You need {points} points more to win a prize."
def is_valid(matrix, row, col):
    return 0 <= row < rows and 0 <= col < rows


def collecting_points(matrix, col):
    total = 0
    for x in range(rows):
        total += int(matrix[x][col])
    return total


points = 0
rows = 6
matrix = []
for row in range(rows):
    matrix.append([x for x in input().split()])

for none in range(3):
    left_strip = input().strip('(')
    right_strip = left_strip.strip(')')
    row, col = right_strip.split(', ')
    row = int(row)
    col = int(col)
    if is_valid(matrix, row, col):
        if matrix[row][col] == 'B':
            matrix[row][col] = 0
            points += collecting_points(matrix, col)

if points <= 99:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
