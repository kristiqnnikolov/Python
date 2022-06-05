# You will be given the coordinates of two points on a Cartesian coordinate system -
# X1, Y1, X2, and Y2 on separate lines.
# Write a function that prints the point which is closest to the center of the coordinate system (0, 0)
# in the format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one.
# The resulting coordinates must be formatted to the lower integer.

from math import floor


def coordinates(x1, y1, x2, y2):
    z1 = abs(x1) + abs(y1)
    z2 = abs(x2) + abs(y2)
    if z1 / 2 <= z2 / 2:
        return f'({floor(x1)}, {floor(y1)})'
    else:
        return f'({floor(x2)}, {floor(y2)})'


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(coordinates(x1, y1, x2, y2))
