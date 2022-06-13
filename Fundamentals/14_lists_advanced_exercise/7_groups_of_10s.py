# Write a program that receives a sequence of numbers (a string containing integers separated by ", ")
# and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.

from math import ceil

numbers = list(map(int, input().split(', ')))

for x in range(1, ceil(max(numbers) / 10) + 1):
    group = list(filter(lambda a: (x - 1) * 10 < a <= x * 10, numbers))
    print(f"Group of {x}0's: {group}")
