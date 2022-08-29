# The pirates need to carry a treasure chest safely back to the ship, looting along the way.
# Create a program that manages the state of the treasure chest along the way.
# On the first line, you will receive the initial loot of the treasure chest,
# which is a string of items separated by a "|".
# "{loot1}|{loot2}|{loot3} … {lootn}"
# The following lines represent commands until "Yohoho!" which ends the treasure hunt:
# •	"Loot {item1} {item2}…{itemn}":
# o	Pick up treasure loot along the way. Insert the items at the beginning of the chest.
# o	If an item is already contained, don't insert it.
# •	"Drop {index}":
# o	Remove the loot at the given position and add it at the end of the treasure chest.
# o	If the index is invalid, skip the command.
# •	"Steal {count}":
# o	Someone steals the last count loot items.
# If there are fewer items than the given count, remove as much as there are.
# o	Print the stolen items separated by ", ":
# "{item1}, {item2}, {item3} … {itemn}"
# In the end, output the average treasure gain, which is the sum of all treasure items
# length divided by the count of all items inside the chest formatted to the second decimal point:
# "Average treasure gain: {averageGain} pirate credits."
# If the chest is empty, print the following message:
# "Failed treasure hunt."

items = input().split('|')
sum_items = 0

while True:
    command = input().split()
    if command[0] == 'Yohoho!':
        break
    elif command[0] == 'Loot':
        for type_items in range(len(command)):
            if type_items == 0:
                continue
            item = command[type_items]
            if item not in items:
                items.insert(0, item)

    elif command[0] == 'Drop':
        idx = int(command[1])
        if idx < len(items):
            x = items.pop(idx)
            items.append(x)
        else:
            continue

    elif command[0] == 'Steal':
        index = int(command[1])
        if index >= len(items):
            removed = items
            print(', '.join(removed))
            print('Failed treasure hunt.')
            exit()
        else:
            removed = items[-index:]
            del items[-index:]
            print(', '.join(removed))

if len(items) > 0:
    for type_items in range(len(items)):
        sum_items += len(items[type_items])
    avg = sum_items / len(items)
    print(f'Average treasure gain: {avg:.2f} pirate credits.')
