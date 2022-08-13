# Heroes III is the best game ever. Everyone loves it and everyone plays it all the time.
# Simon is no exclusion to this rule. His favorite units in the game are all types of dragons –
# black, red, gold, azure etc. He likes them so much that he gives them names and keeps logs of their stats:
# damage, health, and armor. The process of aggregating all the data is quite tedious,
# so he would like to have a program doing it. Since he is no programmer, it's your task to help him.
# You need to categorize dragons by their type. For each dragon, identified by name, keep information about his stats
# (damage, health, and armor). Type is preserved as in the order of input, but dragons are sorted alphabetically by
# their name. For each type, you should also print the average damage, health, and armor of the dragons.
# For each dragon, print his own stats.
# There may be missing stats in the input, though. If a stat is missing you should assign it default values.
# Default values are as follows: health 250, damage 45, and armor 10. Missing stat will be marked by "null".
# The input is in the following format "{type} {name} {damage} {health} {armor}".
# The "type" and the "name" are strings. The "damage", the "health", and the "armor" are integers.
# Any of the integers may be assigned "null" value. See the examples below for better understanding of your task.
# If the same dragon is added a second time, the new stats should overwrite the previous ones.
# Two dragons are considered equal if they match by both name and type.
# Input
# •	On the first line, you are given number N -> the number of dragons to follow.
# •	On the next N lines, you are given input in the above-described format.
# There will be a single space separating each element.
# Output
# •	Print the aggregated data on the console.
# •	For each type, print average stats of its dragons in format "{type}::({damage}/{health}/{armor})".
# •	Damage, health, and armor should be rounded to two digits after the decimal separator.
# •	For each dragon, print its stats in format "-{Name} -> damage: {damage}, health: {health}, armor: {armor}".
dragons = {}
average_stats = {}

for _ in range(int(input())):
    color, name, damage, health, armor = input().split()
    if damage == "null":
        damage = 45
    else:
        damage = int(damage)
    if health == "null":
        health = 250
    else:
        health = int(health)
    if armor == "null":
        armor = 10
    else:
        armor = int(armor)
    if color not in dragons:
        dragons[color] = {name: [damage, health, armor]}
    else:
        dragons[color][name] = [damage, health, armor]

for color, stats in dragons.items():
    damage = []
    health = []
    armor = []
    for name, stat in stats.items():
        damage.append(stat[0])
        health.append(stat[1])
        armor.append(stat[2])
    average_damage = sum(damage) / len(damage)
    average_health = sum(health) / len(health)
    average_armor = sum(armor) / len(armor)
    average_stats[color] = [float(average_damage), float(average_health), float(average_armor)]

for color, stats in average_stats.items():
    print(f"{color}::({stats[0]:.2f}/{stats[1]:.2f}/{stats[2]:.2f})")
    for name, stat in sorted(dragons[color].items(), key=lambda x: x[0]):
        print(f"-{name} -> damage: {stat[0]}, health: {stat[1]}, armor: {stat[2]}")
