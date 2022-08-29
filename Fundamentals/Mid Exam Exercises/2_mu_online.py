# You have initial health 100 and initial bitcoins 0. You will be given a string representing the dungeon's rooms.
# Each room is separated with '|' (vertical bar): "room1|room2|room3…"
# Each room contains a command and a number, separated by space. The command can be:
# •	"potion"
# o	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
# o	First print: "You healed for {amount} hp."
# o	After that, print your current health: "Current health: {health} hp."
# •	"chest"
# o	You've found some bitcoins, the number in the second part.
# o	Print: "You found {amount} bitcoins."
# •	In any other case, you are facing a monster, which you will fight.
# The second part of the room contains the attack of the monster.
# You should remove the monster's attack from your health.
# o	If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
# o	If you've died, print "You died! Killed by {monster}." and your quest is over.
# Print the best room you've manage to reach: "Best room: {room}"
# If you managed to go through all the rooms in the dungeon, print on the following three lines:
# "You've made it!"
# "Bitcoins: {bitcoins}"
# "Health: {health}"

dungeon = input().split('|')
health = 100
bitcoins = 0
index = 0
for current_command in dungeon:
    command = current_command.split(' ')
    item = command[0]
    value = int(command[1])
    if item == 'potion':
        if value > 100 - health:
            print(f"You healed for {100 - health} hp.")
        else:
            print(f"You healed for {value} hp.")
        health += value
        if health > 100:
            health = 100
        print(f"Current health: {health} hp.")
    elif item == 'chest':
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health > 0:
            print(f"You slayed {item}.")
        else:
            print(f"You died! Killed by {item}.")
            print(f"Best room: {index + 1}")
            break
    index += 1
if health > 0:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
