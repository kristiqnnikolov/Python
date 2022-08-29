# Write a program that recreates the Memory game.
# On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin.
# Until the player receives "end" from the console, you will receive strings with two integers separated by a space,
# representing the indexes of elements in the sequence.
# If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence,
# you should add two matching elements at the middle of the sequence in the following format:
# "-{number of moves until now}a"
# Then print this message on the console:
# "Invalid input! Adding additional elements to the board"

def is_valid(index, len_list):
    if index in range(len_list):
        return True
    return False


elements = input().split()
rounds = 0
you_lose = False
while True:
    if not elements:
        print(f"You have won in {rounds} turns!")
        break
    command = input().split()
    if command[0] == 'end':
        break
    index_1 = int(command[0])
    index_2 = int(command[1])
    rounds += 1
    if is_valid(index_1, len(elements)) and is_valid(index_2, len(elements)) and index_1 != index_2:
        first = elements[index_1]
        second = elements[index_2]
        if first == second:
            elements.remove(first)
            elements.remove(second)
            print(f"Congrats! You have found matching elements - {first}!")
        else:
            print(f"Try again!")
    else:
        adding = f'-{rounds}a'
        middle = len(elements) // 2
        elements.insert(middle, adding)
        elements.insert(middle, adding)
        print("Invalid input! Adding additional elements to the board")
if elements:
    print(f"Sorry you lose :(")
    print(*elements, sep=' ')
