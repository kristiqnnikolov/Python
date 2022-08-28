# You are a world traveler, and your next goal is to make a world tour.
# To do that, you have to plan out everything first.
# To start with, you would like to plan out all of your stops where you will have a break.
# On the first line, you will be given a string containing all of your stops.
# Until you receive the command "Travel", you will be given some commands to manipulate that initial string.
# The commands can be:
# •	"Add Stop:{index}:{string}":
# o	Insert the given string at that index only if the index is valid
# •	"Remove Stop:{start_index}:{end_index}":
# o	Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# •	"Switch:{old_string}:{new_string}":
# o	If the old string is in the initial string, replace it with the new one (all occurrences)
# Note: After each command, print the current state of the string
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"

text = input()
current_command = input()
while not current_command == 'Travel':
    command = current_command.split(":")
    action = command[0]
    if action == 'Add Stop':
        index = int(command[1])
        txt = command[2]
        if len(text) >= index:
            for i in range(len(text)):
                if index == i:
                    start = text[:index]
                    end = text[index:]
                    text = start + txt + end
                    break
        print(text)
    elif action == 'Remove Stop':
        start = int(command[1])
        end = int(command[2]) + 1
        if start <= len(text) >= end:
            first = text[:start]
            second = text[end:]
            text = first + second
        print(text)
    elif action == 'Switch':
        old = command[1]
        new = command[2]
        if old in text:
            text = text.replace(old, new)
        print(text)
    current_command = input()
print(f"Ready for world tour! Planned stops: {text}")
