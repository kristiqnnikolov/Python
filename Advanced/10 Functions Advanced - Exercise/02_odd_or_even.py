# On the first line, you will receive a command - "Odd" or "Even".
# You will receive a sequence of numbers (integers) on the second line, separated by a single space.
# •	If the command is "Odd", print the sum of the odd numbers multiplied by the count of all numbers.
# •	If the command is "Even", print the sum of the even numbers multiplied by the count of all numbers.
def odd_or_even(command, nums):
    if command == 'Odd':
        return sum([int(x) for x in nums if x % 2 == 1]) * len(nums)
    elif command == 'Even':
        return sum([int(x) for x in nums if x % 2 == 0]) * len(nums)


odd_or_even_command = input()
numbers = [int(x) for x in input().split()]
print(odd_or_even(odd_or_even_command, numbers))
