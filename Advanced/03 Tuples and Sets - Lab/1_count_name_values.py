# You will be given numbers separated by a space.
# Write a program that prints the number of occurrences of each number in the format "{number} - {count} times".
# The number must be formatted to the first decimal point.

numbers = tuple(map(float, input().split()))

filtered = {}
for num in numbers:
    if num not in filtered:
        filtered[num] = 0
    filtered[num] += 1

for key, value in filtered.items():
    print(f'{key} - {value} times')