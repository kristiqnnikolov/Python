# Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
# You will receive a 6x6 field on separate lines with:
# •	One rover - marked with the letter "E"
# •	Water deposit (one or many) - marked with the letter "W"
# •	Metal deposit (one or many) - marked with the letter "M"
# •	Concrete deposit (one or many) - marked with the letter "C"
# •	Rock (one or many) - marked with the letter "R"
# •	Empty positions will be marked with "-"
# After that, you will be given the commands for the rover's movement on one line
# separated by a comma and a space (", "). Commands can be: "up", "down", "left", or "right".
# For each command, the rover moves in the given directions with one step,
# and it can land on one of the given types of deposit or a rock:
# •	When it lands on a deposit, you must print the coordinates of that
# deposit in the format shown below and increase its value by 1.
# •	If the rover lands on a rock, it gets broken. Print the coordinates
# where it got broken in the format shown below, and the program ends.
# •	If the rover goes out of the field, it should continue from the opposite side in the same direction.
# Example: If the rover is at position (3, 0) and it needs to move left (outside the matrix),
# it should be placed at position (3, 5).
# The rover needs to find at least one of each deposit to consider the area suitable to start our colony.
# Stop the program if you run out of commands or the rover gets broken.
# Input
# •	On the first 6 lines, you will receive the matrix.
# •	On the following line, you will receive the commands for the rover separated by a comma and a space.
# Output
# •	For each deposit found while you go through the commands, print out on the console:
# "{Water, Metal or Concrete} deposit found at ({row}, {col})"
# •	If the rover hits a rock, print the coordinates where it got broken in the format:
# "Rover got broken at ({row}, {col})"
# After you go through all the commands or the rover gets broken, print out on the console:
# •	If the rover has found at least one of each deposit, print on the console: "Area suitable to start the colony."
# •	Otherwise, print on the console: "Area not suitable to start the colony."
def next_move(command, row, col):
    if command == 'up':
        if row - 1 < 0:
            return 5, col
        else:
            return row - 1, col
    if command == 'left':
        if col - 1 < 0:
            return row, 5
        else:
            return row, col - 1
    if command == 'right':
        if col + 1 > 5:
            return row, 0
        else:
            return row, col + 1
    if command == 'down':
        if row + 1 > 5:
            return 0, col
        else:
            return row + 1, col


rows = 6
matrix = []
rover_row = 0
rover_col = 0
water = False
metal = False
concrete = False
for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "E":
            rover_row = row
            rover_col = col

commands = input().split(", ")
for command in commands:
    next_row, next_col = next_move(command, rover_row, rover_col)

    if matrix[next_row][next_col] == 'R':
        print(f"Rover got broken at ({next_row}, {next_col})")
        break
    elif matrix[next_row][next_col] == 'W':
        print(f"Water deposit found at ({next_row}, {next_col})")
        water = True
    elif matrix[next_row][next_col] == 'M':
        print(f"Metal deposit found at ({next_row}, {next_col})")
        metal = True
    elif matrix[next_row][next_col] == 'C':
        print(f"Concrete deposit found at ({next_row}, {next_col})")
        concrete = True
    matrix[next_row][next_col] = 'E'
    matrix[rover_row][rover_col] = '-'
    rover_row, rover_col = next_row, next_col

if water and concrete and metal:
    print(f"Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
