# You are participating in a Firearm course. It is a training day at the shooting range.
# You will be given a matrix with 5 rows and 5 columns.
# It is a shotgun range represented as some symbols separated by a single space:
# •	Your position is marked with the symbol "A"
# •	Targets marked with symbol "x"
# •	All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive.
# The possible commands are:
# •	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps.
# You can only move if the field you want to step on is marked with ".".
# •	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving).
# Beware that there might be targets that stand in the way of other targets, and you cannot reach them
# you can shoot only the nearest target. When you have shot a target, the field becomes empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
# •	If at any point there are no targets left, end the program and print:
# "Training completed! All {count_targets} targets hit.".
# •	If, after you perform all the commands, there are some targets left print:
# "Training not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the examples.
# Input
# •	5 lines representing the field (symbols, separated by a single space)
# •	N - count of commands
# •	On the following N lines - the commands in the format described above
# Output
# •	On the first line, print one of the following:
# o	If all the targets were shot
# "Training completed! All {count_targets} targets hit."
# o	Otherwise:
#               	       "Training not completed! {count_left_targets} targets left."
# •	Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.
def next_move(direction, row, col, step):
    if direction == 'up':
        return row - step, col
    if direction == 'left':
        return row, col - step
    if direction == 'right':
        return row, col + step
    if direction == 'down':
        return row + step, col


def is_out(row, col):
    return 0 > row or row >= 5 or 0 > col or col >= 5


matrix = []
position_row = 0
position_col = 0
targets = 0


for row in range(5):
    matrix.append([x for x in input().split()])
    for col in range(5):
        if matrix[row][col] == "A":
            position_row = row
            position_col = col
        elif matrix[row][col] == 'x':
            targets += 1

number_commands = int(input())
hits = []
targets_left = targets

for none in range(number_commands):
    command = input().split()
    direction = command[1]
    if command[0] == 'move':
        steps = int(command[2])
        next_row, next_col = next_move(direction, position_row, position_col, steps)
        if is_out(next_row, next_col) or matrix[next_row][next_col] != '.':
            continue

        matrix[position_row][position_col] = '.'
        position_row, position_col = next_row, next_col
        matrix[position_row][position_col] = 'A'
    elif command[0] == 'shoot':
        shoot_row, shoot_col = position_row, position_col
        while True:
            shoot_row, shoot_col = next_move(direction, shoot_row, shoot_col, 1)
            if is_out(shoot_row, shoot_col):
                break
            if matrix[shoot_row][shoot_col] == 'x':
                targets_left -= 1
                matrix[shoot_row][shoot_col] = '.'
                hits.append([shoot_row, shoot_col])
                break
        if targets_left == 0:
            print(f"Training completed! All {targets} targets hit.")
            break

if targets_left != 0:
    print(f"Training not completed! {targets_left} targets left.")
for hit in hits:
    print(hit)
