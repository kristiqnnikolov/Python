# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough.
# However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
# •	"Shadowmourne" - requires 250 Shards
# •	"Valanyr" - requires 250 Fragments
# •	"Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race.
# At that point, you have to print that the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.

def obtained(dictionary, item):
    for key, value in dictionary.items():
        if value >= 250:
            dictionary[key] -= 250
            if item == "shards":
                print("Shadowmourne obtained!")
                for key, value in dictionary.items():
                    print(f'{key}: {value}')
                exit()
            elif item == "fragments":
                print("Valanyr obtained!")
                for key, value in dictionary.items():
                    print(f'{key}: {value}')
                exit()
            elif item == "motes":
                print("Dragonwrath obtained!")
                for key, value in dictionary.items():
                    print(f'{key}: {value}')
                exit()


command = input().split()
dictionary = {'shards': 0, 'fragments': 0, 'motes': 0}
while True:
    for index in range(0, len(command), 2):
        value = int(command[index])
        item = command[index + 1].lower()
        if item in dictionary:
            dictionary[item] += value
            if dictionary['shards'] >= 250:
                obtained(dictionary, item)
            elif dictionary['fragments'] >= 250:
                obtained(dictionary, item)
            elif dictionary['motes'] >= 250:
                obtained(dictionary, item)

        else:
            dictionary[item] = value
    command = input().split()
