# Write a program to read a sequence of integers and find and print the top 5 numbers greater than
# the average value in the sequence, sorted in descending order.

numbers = input().split()
current_command = input()
while current_command != 'Finish':
    command = current_command.split()
    if command[0] == 'Add':
        number = command[1]
        numbers.append(number)
    elif command[0] == 'Remove':
        number = command[1]
        if number in numbers:
            numbers.remove(number)
    elif command[0] == 'Replace':
        number = command[1]
        replaces = command[2]
        if number in numbers:
            index = numbers.index(number)
            numbers.insert(index, replaces)
            numbers.pop(index + 1)
    elif command[0] == 'Collapse':
        value = int(command[1])
        numbers = list(filter(lambda x: int(x) >= value, numbers))
    current_command = input()
print(*numbers, sep=' ')
