# You will be receiving to-do notes until you get the command "End".
# The notes will be in the format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).

command = input()
new_list = [0] * 20
while not command == "End":
    index, string = command.split('-')
    index = int(index)
    new_list[index] = string
    command = input()
print([string for string in new_list if not string == 0])
