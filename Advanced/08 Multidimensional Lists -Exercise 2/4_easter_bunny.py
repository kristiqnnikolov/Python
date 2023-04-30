# Your task is to collect as many eggs as possible.
# On the first line, you will be given a number representing the size of the field.
# On the following few lines, you will be given a field with:
# •	One bunny - randomly placed in it and marked with the symbol "B"
# •	Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
# The directions that should be considered as possible are up, down, left, and right.
# If you reach a trap while checking some of the directions,
# you should not consider the fields after the trap in this direction. For more clarifications, see the examples below.
# Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
# Input
# •	A number representing the size of the field
# •	The matrix representing the field (each position separated by a single space)
# Output
# •	The direction which should be considered as best (lowercase)
# •	The field positions from which we are collecting eggs as lists
# •	The total number of eggs collected
def is_valid(matrix, row, col):
    if 0 <= row < rows and 0 <= col < rows and not matrix[row][col] == "X":
        return True
    return False


rows = int(input())
matrix = []

points = {
    "up": [0, False],
    "down": [0, False],
    "left": [0, False],
    "right": [0, False]
}
coordinates = {
    "up": [],
    "down": [],
    "left": [],
    "right": []
}
bunny_row = 0
bunny_col = 0

for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "B":
            bunny_row = row
            bunny_col = col

for row in range(bunny_row - 1, -1, -1):
    if is_valid(matrix, row, bunny_col) and not matrix[row][bunny_col] == 'B':
        points["up"][0] += int(matrix[row][bunny_col])
        points["up"][1] = True
        coordinates["up"].append([row, bunny_col])
    else:
        break
for row in range(bunny_row + 1, rows):
    if is_valid(matrix, row, bunny_col) and not matrix[row][bunny_col] == 'B':
        points["down"][0] += int(matrix[row][bunny_col])
        points["down"][1] = True
        coordinates["down"].append([row, bunny_col])
    else:
        break
for col in range(bunny_col - 1, -1, -1):
    if is_valid(matrix, bunny_row, col) and not matrix[bunny_row][col] == 'B':
        points["left"][0] += int(matrix[bunny_row][col])
        points["left"][1] = True
        coordinates["left"].append([bunny_row, col])
    else:
        break
for col in range(bunny_col + 1, rows):
    if is_valid(matrix, bunny_row, col) and not matrix[bunny_row][col] == 'B':
        points["right"][0] += int(matrix[bunny_row][col])
        points["right"][1] = True
        coordinates["right"].append([bunny_row, col])
    else:
        break

for key, value in points.items():
    if not value[1]:
        points[key] = [-1, False]

max_points_direction = max(points, key=lambda x: points[x])
print(max_points_direction)
for direction in coordinates[max_points_direction]:
    print(direction)
print(points[max_points_direction][0])
