# Write a program that reads a matrix from the console and changes its values. On the first line,
# you will get the matrix's rows - N. You will get elements for each column on the following N lines,
# separated with a single space. You will be receiving commands in the following format:
# •	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
# •	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates".
# A coordinate is valid if both of the given indexes are in range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.
def the_matrix():
    matrix = []
    rows = int(input())
    for none in range(rows):
        matrix.append([int(x) for x in input().split()])
    return matrix


matrix = the_matrix()
command = input()

while not command == 'END':
    commands = command.split()
    row = int(commands[1])
    col = int(commands[2])
    value = int(commands[3])
    if commands[0] == 'Add':
        if row >= 0 <= col:
            try:
                matrix[row][col] += value
            except IndexError:
                print("Invalid coordinates")
        else:
            print("Invalid coordinates")
    elif commands[0] == 'Subtract':
        if row >= 0 <= col:
            try:
                matrix[row][col] -= value
            except IndexError:
                print("Invalid coordinates")
        else:
            print("Invalid coordinates")
    command = input()

for rows in matrix:
    print(*rows)
