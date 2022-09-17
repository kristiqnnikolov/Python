# On the first line, you will receive a string of numbers separated by space.
# On the second line, you'll receive a target number. Your task is to find
# all pairs of numbers whose sum equals the target number.
# For each found pair print "{number} + {number} = {target_number}".
# Then, save only the unique pairs. Note: (1, 2) and (2, 1) are unique.
# Also, you should keep track of how many iterations you've done.
# At the end print all the iterations done in format: "Iterations done: {total_number_of_iterations}".
# On the following lines, print the unique pairs in the format: "(first_number, second_number)".
# The order in which we print the result does not matter.
from collections import deque

numbers = deque([int(x) for x in input().split()])
target = int(input())
counter = 0
pair = []
unique_pair = set()

while len(numbers) > 0:
    for i in range(len(numbers) - 1):
        counter += 1
        if numbers[0] + numbers[i + 1] == target:
            unique_pair.add(tuple([numbers[0], numbers[i + 1]]))
            pair = []
            print(f"{numbers[0]} + {numbers[i + 1]} = {target}")
    numbers.popleft()

print(f"Iterations done: {counter}")
[print(x) for x in unique_pair]
