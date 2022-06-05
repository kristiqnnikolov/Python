# You will be given the coordinates of four points. The first and the second pair of points form two different lines.
# Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})"
# starting from the point which is closer to the center of the coordinate system (0, 0).
# You can reuse the method that you wrote for the previous problem.
# If the lines are of equal length, print only the first one.
# The resulting coordinates must be formatted to the lower integer.

from math import floor


def coordinates(x1, y1, x2, y2, x3, y3, x4, y4):
    z1 = (abs(x1) + abs(y1)) / 2
    z2 = (abs(x2) + abs(y2)) / 2
    z3 = (abs(x3) + abs(y3)) / 2
    z4 = (abs(x4) + abs(y4)) / 2
    if (z1 + z2) > (z3 + z4):
        if z1 >= z2:
            return f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})'
        elif z1 < z2:
            return f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})'
    else:
        if z3 > z4:
            return f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})'
        elif z3 <= z4:
            return f'({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})'


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
print(coordinates(x1, y1, x2, y2, x3, y3, x4, y4))
