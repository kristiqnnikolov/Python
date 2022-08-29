# You are given an array with integers. Write a program to modify the elements after receiving the following commands:
# •	"swap {index1} {index2}" takes two elements and swap their places.
# •	"multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index.
# Save the product at the 1st index.
# •	"decrease" decreases all elements in the array with 1.

data = input()
array = [int(x) for x in data.split()]
current_command = input()
while current_command != 'end':
    command = current_command.split()
    if command[0] == 'swap':
        swap = int(command[1])
        swap_with = int(command[2])
        array[swap], array[swap_with] = array[swap_with], array[swap]
    elif command[0] == 'multiply':
        multiply = int(command[1])
        by = int(command[2])
        array[multiply] = int(array[multiply]) * int(array[by])
    elif command[0] == 'decrease':
        array = [n - 1 for n in array]
    current_command = input()
print(*array, sep=", ")
