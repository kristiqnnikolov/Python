# Write a program that reads a matrix from the console and performs certain operations with its elements.
# User input is provided similarly to the problems above - first, you read the dimensions and then the data.
# Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and
# ("row2", "col2") are the coordinates of two points in the matrix.
# A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less),
# separated by a single space.
# •	If the command is valid, you should swap the values at the given indexes and print the matrix at each step
# (thus, you will be able to check if the operation was performed correctly).
# •	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, or
# the given coordinates are not valid), print "Invalid input!" and move on to the following command.
# A negative value makes the coordinates not valid.
# Your program should finish when the command "END" is entered.

def the_matrix(rows):
    matrix = []
    for none in range(rows):
        matrix.append([x for x in input().split()])
    return matrix


def valid_index(r1, c1, row, col):
    return 0 <= r1 < row and 0 <= c1 < col


rows, cols = [int(x) for x in input().split()]
matrix = the_matrix(rows)

command = input()
while not command == 'END':
    commands = command.split()
    if len(commands) == 5 and commands[0] == 'swap':
        row1, col1, row2, col2 = [int(x) for x in commands[1:]]
        if valid_index(row1, col1, rows, cols) and \
                valid_index(row2, col2, rows, cols):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for row in matrix:
                print(' '.join([str(x) for x in row]))
        else:
            print("Invalid input!")

    else:
        print("Invalid input!")
    command = input()
