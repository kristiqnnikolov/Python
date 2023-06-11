# You are visiting Santa Claus' workshop, and it is complete chaos.
# You will need to help Santa find all items scattered around the workshop.
# You will be given the size of the matrix in the format "{rows}, {columns}".
# It is the Santa's workshop represented as some symbols separated by a single space:
# •	Your position is marked with the symbol "Y"
# •	Christmas decorations are marked with the symbol "D"
# •	Gifts are marked with the symbol "G"
# •	Cookies are marked with the symbol "C"
# •	All of the empty positions will be marked with "."
# After the field state, you will be given commands until you receive the command "End".
# The commands will be in the format "right/left/up/down-{steps}".
# You should move in the given direction with the given steps and collect all the items that come across.
# If you go out of the field, you should continue to traverse the field from the opposite side in the same direction.
# You should mark your path with "x". Your current position should always be marked with "Y".
# Keep track of all collected items. If you've collected all items at any point,
# end the program and print: "Merry Christmas!".
# Input
# •	On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
# •	On the next lines, you will receive each row with its columns - symbols, separated by a single space.
# •	On the following lines, you will receive commands in the format described above until you receive
# the command "End" or until you collect all items.
# Output
# •	On the first line, if you have collected all items, print:
# o	"Merry Christmas!"
# o	Otherwise, skip the line
# •	Next, print the number of collected items in the format:
# o	"You've collected:
# o	- {number_of_decoration} Christmas decorations
# o	- {number_of_gifts} Gifts
# o	- {number_of_cookies} Cookies"
# •	Finally, print the field, as shown in the examples.
def next_move(command, row, col, rows, cols):
    if command == 'up':
        if row - 1 < 0:
            return rows - 1, col
        else:
            return row - 1, col
    if command == 'left':
        if col - 1 < 0:
            return row, cols - 1
        else:
            return row, col - 1
    if command == 'right':
        if col + 1 >= cols:
            return row, 0
        else:
            return row, col + 1
    if command == 'down':
        if row + 1 >= rows:
            return 0, col
        else:
            return row + 1, col


rows, cols = [int(x) for x in input().split(', ')]
matrix = []
santa_row = 0
santa_col = 0
gifts = 0
cookies = 0
decorations = 0
collected_gifts = 0
collected_cookies = 0
collected_decorations = 0
all_collected = False
for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(cols):
        if matrix[row][col] == 'Y':
            santa_row = row
            santa_col = col
        elif matrix[row][col] == 'D':
            decorations += 1
        elif matrix[row][col] == 'G':
            gifts += 1
        elif matrix[row][col] == 'C':
            cookies += 1


while True:
    if all_collected:
        break
    command = input()
    if command == 'End':
        break
    commands = command.split('-')
    direction = commands[0]
    steps = int(commands[1])

    while steps and not all_collected:
        next_row, next_col = next_move(direction, santa_row, santa_col, rows, cols)
        steps -= 1
        if matrix[next_row][next_col] == 'D':
            decorations -= 1
            collected_decorations += 1
        elif matrix[next_row][next_col] == 'C':
            cookies -= 1
            collected_cookies += 1
        elif matrix[next_row][next_col] == 'G':
            gifts -= 1
            collected_gifts += 1

        matrix[santa_row][santa_col] = 'x'
        santa_row, santa_col = next_row, next_col
        matrix[next_row][next_col] = 'Y'
        if not gifts:
            if not cookies:
                if not decorations:
                    all_collected = True

if all_collected:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {collected_decorations} Christmas decorations")
print(f"- {collected_gifts} Gifts")
print(f"- {collected_cookies} Cookies")
for row in matrix:
    print(*row)
