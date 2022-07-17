# Write a program that announces the winner of a car race.
# You will receive a sequence of numbers.
# Each number represents the time needed for the car to pass through that step (the index).
# There will be two cars. The first one starts from the left side, and the other one starts from the right side.
# The middle index of the sequence is the finish line.
# Calculate the total time each racer needs to reach the finish line and print the winner with his total time
# (the racer with less time). If you have a zero in the list,
# you should reduce the racer's time that reached it by 20% (from his current time).
# The number of elements in the sequence will always be odd.
# Print the result in the following format "The winner is {left/right} with total time: {total_time}".
# The time should be formatted to the first decimal point.

numbers = input().split(" ")
final = len(numbers) // 2
total_left = 0
total_right = 0
result = ""

for left_index in range(final):
    left_as_int = int(numbers[left_index])
    if left_as_int == 0:
        total_left -= total_left * 0.2
    else:
        total_left += left_as_int
for right_index in range(len(numbers) - 1, final, -1):
    right_as_int = int(numbers[right_index])
    if right_as_int == 0:
        total_right -= total_right * 0.2
    else:
        total_right += right_as_int

if total_left > total_right:
    print(f"The winner is right with total time: {total_right:.1f}")
else:
    print(f"The winner is left with total time: {total_left:.1f}")

print(result)
