# Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
# You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines,
# you will receive the rows of the territory:
# •	Alice will be placed in a random position, marked with the letter "A".
# •	On the territory, there will be bags of tea, represented as numbers.
# If Alice steps on a number position, she collects the tea bags and increases the quantity with the corresponding number.
# •	There will always be one rabbit hole on the territory marked with the letter "R".
# •	All of the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements.
# Move commands can be: "up", "down", "left" or "right".
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party,
# and she does not need to continue collecting. Otherwise,
# if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends.
# In the end, the path she walked had to be marked with '*'.
# For more clarifications, see the examples below.
# Input
# •	On the first line, you will be given the integer n – the size of the square matrix
# •	On the following n lines - matrix representing the field (each position separated by a single space)
# •	On each of the following lines, you will be given a move command
# Output
# •	On the first line:
# o	If Alice steps on the rabbit hole or she go out of the territory, print:
# "Alice didn't make it to the tea party."
# o	If she collected at least 10 bags of tea, print:
# "She did it! She went to the party."
# •	On the following lines, print the matrix.
def next_move(command, row, col):  # функция посоки
    if command == 'up':
        return row - 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1
    if command == 'down':
        return row + 1, col


def printing_matrix(matrix):
    for row in matrix:
        print(*row, sep=' ')


rows = int(input())
matrix = []
alice_row = 0
alice_col = 0
tea = 0

for row in range(rows):  # пълним матрицата и намираме Алис
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "A":
            alice_row = row
            alice_col = col

while tea <= 9:  # докато чая е под 9 вкл. четем команди
    command = input()
    next_row, next_col = next_move(command, alice_row, alice_col)  # следващ ход

    if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= rows:  # ако следващия ход е извън матрицата
        matrix[alice_row][alice_col] = "*"  # заместваме стария със * и принтираме
        print("Alice didn't make it to the tea party.")
        printing_matrix(matrix)
        break
    if matrix[next_row][next_col] in '1234567890 10':  # ако следващия ход е число , прибавяме към чая
        tea += int(matrix[next_row][next_col])
        matrix[alice_row][alice_col] = "*"  # слагаме * на старото място и А на новото
        matrix[next_row][next_col] = "A"
    elif matrix[next_row][next_col] == 'R':  # ако следващия ход е заешка дупка
        matrix[next_row][next_col] = "*"
        matrix[alice_row][alice_col] = "*"  # слагаме * на старото място и * на новото и принтираме
        print("Alice didn't make it to the tea party.")
        printing_matrix(matrix)
        break
    else:
        matrix[alice_row][alice_col] = "*"  # ако следващия ход е . запаметяваме и заместваме с А
        matrix[next_row][next_col] = "A"
    alice_row, alice_col = next_row, next_col
if tea >= 10:
    matrix[alice_row][alice_col] = '*'
    print("She did it! She went to the party.")
    printing_matrix(matrix)
