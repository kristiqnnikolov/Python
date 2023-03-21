# Using a nested list comprehension, write a program that reads rows of a square matrix and its elements,
# separated by a comma and a space ", ".
# You should find the matrix's diagonals, prints them and their sum in the format:
# "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
# Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".

def the_matrix(rows):
    matrix = []
    for none in range(rows):
        matrix.append([int(x) for x in input().split(", ")])
    return matrix


lines = int(input())
matrix = the_matrix(lines)
primary = 0
secondary = 0
primary_list = []
secondary_list = []
for row in range(lines):
    for col in range(lines - 1, -1, -1):
        if row + col == lines - 1:
            secondary += matrix[row][col]
            secondary_list.append(str(matrix[row][col]))
        if row == col:
            primary += matrix[row][col]
            primary_list.append(str(matrix[row][col]))
print(f"Primary diagonal: {', '.join(primary_list)}. Sum: {primary}")
print(f"Secondary diagonal: {', '.join(secondary_list)}. Sum: {secondary}")
