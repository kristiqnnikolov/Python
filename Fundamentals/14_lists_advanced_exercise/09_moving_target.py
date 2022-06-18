# You are at the shooting gallery again, and you need a program that helps you keep track of moving targets.
# On the first line, you will receive a sequence of targets with their integer values, split by a single space.
# Then, you will start receiving commands for manipulating the targets until the "End" command.
# The commands are the following:
# •	"Shoot {index} {power}"
# o	Shoot the target at the index if it exists by reducing its value by the given power (integer value).
# A target is considered shot when its value reaches 0.
# o	Remove the target if it is shot.
# •	"Add {index} {value}"
# o	Insert a target with the received value at the received index if it exists. If not, print: "Invalid placement!"
# •	"Strike {index} {radius}"
# o	Remove the target at the given index (if such exist) and the ones before and after it depending on the radius.
# o	If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
#  Example:  "Strike 2 2"
# 	{radius}	{radius}	{strikeIndex}	{radius}	{radius}
#
# •	"End"
# o	Print the sequence with targets in the following format:
# "{target1}|{target2} … |{targetn}"

def is_valid(index, len):
    if index in range(len):
        return True
    return False


numbers = list(map(int, input().split()))
while True:
    command = input().split()
    if command[0] == 'End':
        break
    elif command[0] == 'Shoot':
        index = int(command[1])
        power = int(command[2])
        if is_valid(index, len(numbers)):
            numbers[index] -= power
            if numbers[index] <= 0:
                numbers.pop(index)
    elif command[0] == 'Add':
        index = int(command[1])
        value = int(command[2])
        if is_valid(index, len(numbers)):
            numbers.insert(index, value)
        else:
            print("Invalid placement!")
    elif command[0] == 'Strike':
        index = int(command[1])
        radius = int(command[2])
        left_side = index - radius
        right_side = index + radius
        if is_valid(index, len(numbers)):
            if is_valid(left_side, len(numbers)):
                if is_valid(right_side, len(numbers)):
                    left_part = numbers[:left_side]
                    right_part = numbers[right_side + 1:]
                    numbers = left_part + right_part
            else:
                print("Strike missed!")
print(*[str(el) for el in numbers], sep="|")
