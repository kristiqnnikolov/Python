# Snow White loves her dwarfs, but there are so many, and she doesn't know how to order them.
# Does she order them by name? Or by color of their hat? Or by physics?
# She can't decide, so it's up to you to write a program that does it for her.
# You will be receiving several input lines which contain data about each dwarf in the following format:
# {dwarf_name} <:> {dwarf_hat_color} <:> {dwarf_physics}
# The "dwarf_name" and the "dwarf_hat_color" are strings. The "dwarf_physics" is an integer.
# You must store the data about the dwarfs in your program. There are several rules though:
# •	If 2 dwarfs have the same name but different color,
# they should be considered different dwarfs, and you should store them both.
# •	If 2 dwarfs have the same name and the same color, store the one with the higher physics.
# When you receive the command "Once upon a time", the input ends.
# You must order the dwarfs by physics in descending order and then by
# total count of dwarfs with the same hat color in descending order.
# Then you must print them all.
# Input
# •	The input will consist of several input lines, containing dwarf data in the format, specified above.
# •	The input ends when you receive the command "Once upon a time".
# Output
# •	As output, you must print the dwarfs, ordered in the way, specified above.
# •	The output format is: "({hat_color}) {name} <-> {physics}"
dwarfs = {}
colors = {}
while True:
    command = input()
    if command == "Once upon a time":
        break
    tokens = command.split(" <:> ")
    name = tokens[0]
    color = tokens[1]
    physics = int(tokens[2])
    id = name + ":" + color
    if id not in dwarfs:
        if color not in colors:
            colors[color] = 1
        else:
            colors[color] += 1
        dwarfs[id] = [0, color]
    dwarfs[id][0] = max([dwarfs[id][0], physics])

sorted_dwrafs = dict(sorted(dwarfs.items(), key=lambda x: (x[1][0], colors[x[1][1]]), reverse=True))
for key, value in sorted_dwrafs.items():
    tokens = key.split(":")
    print(f"({tokens[1]}) {tokens[0]} <-> {value[0]}")