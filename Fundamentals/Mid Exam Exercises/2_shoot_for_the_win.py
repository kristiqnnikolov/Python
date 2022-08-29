# Write a program that helps you keep track of your shot targets.
# You will receive a sequence with integers, separated by a single space, representing targets and their value.
# Afterward, you will be receiving indices until the "End" command is given, and you need to print
# the targets and the count of shot targets.
# Every time you receive an index, you need to shoot the target on that index, if it is possible.
# Every time you shoot a target, its value becomes -1, and it is considered shot. Along with that, you also need to:
# •	Reduce all the other targets, which have greater values than your current target, with its value.
# •	Increase all the other targets, which have less than or equal value to the shot target, with its value.
# Keep in mind that you can't shoot a target, which is already shot.
# You also can't increase or reduce a target, which is considered shot.
# When you receive the "End" command, print the targets in their current state and
# the count of shot targets in the following format:
# "Shot targets: {count} -> {target1} {target2}… {targetn}"

numbers = input()
targets = [int(x) for x in numbers.split()]
current_command = input()
shots = 0
while current_command != 'End':
    command = int(current_command)
    if command not in range(len(targets)):
        current_command = input()
        continue
    value = targets[command]
    if value == -1:
        current_command = input()
        continue

    for index in range(len(targets)):
        if targets[index] == -1:
            continue
        if targets[index] > value:
            targets[index] -= value
        else:
            targets[index] += value
    targets[command] = -1
    shots += 1
    current_command = input()
target = [str(x) for x in targets]
print(f"Shot targets: {shots} -> {(' '.join(target))}")
