# You will receive an initial list with groceries separated by an exclamation mark "!".
# After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
# •	"Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
# •	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list.
# Otherwise, skip this command.
# •	"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one.
# Otherwise, skip this command.
# •	"Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at
# the end of the list. Otherwise, skip this command.

groceries = input().split("!")
current_command = input()
while current_command != 'Go Shopping!':
    command = current_command.split(" ")
    if command[0] == 'Urgent':
        item = command[1]
        if item not in groceries:
            groceries.insert(0, item)
    elif command[0] == 'Unnecessary':
        item = command[1]
        if item in groceries:
            groceries.remove(item)
    elif command[0] == 'Correct':
        old_item = command[1]
        new_item = command[2]
        if old_item in groceries:
            index_old = groceries.index(old_item)
            groceries.remove(old_item)
            groceries.insert(index_old, new_item)
    elif command[0] == 'Rearrange':
        item = command[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
    current_command = input()
print(*groceries, sep=', ')
