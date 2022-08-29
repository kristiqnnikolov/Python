# Create a program that tracks the battle and either chooses a winner or prints a stalemate.
# On the first line, you will receive the status of the pirate ship,
# which is a string representing integer sections separated by ">".
# On the second line, you will receive the same type of status, but for the warship:
# "{section1}>{section2}>{section3}… {sectionn}"
# On the third line, you will receive the maximum health capacity a section of the ship can reach.
# The following lines represent commands until "Retire":
# •	"Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section.
# Check if the index is valid and if not, skip the command.
# If the section breaks (health <= 0) the warship sinks, print the following and stop the program:
# "You won! The enemy ship has sunken."
# •	"Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship with the given damage at that range
# (indexes are inclusive). Check if both indexes are valid and if not, skip the command.
# If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
# "You lost! The pirate ship has sunken."
# •	"Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health.
# Check if the index is valid and if not, skip the command.
# The health of the section cannot exceed the maximum health capacity.
# •	"Status" - prints the count of all sections of the pirate ship that need repair soon,
# which are all sections that are lower than 20% of the maximum health capacity. Print the following:
# "{count} sections need repair."
# In the end, if a stalemate occurs, print the status of both ships,
# which is the sum of their individual sections, in the following format:
# "Pirate ship status: {pirateShipSum}
# Warship status: {warshipSum}"

pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
max_health = int(input())
is_down = False

while True:
    command = input().split()
    if command[0] == "Retire":
        break

    elif command[0] == "Fire":
        current_index = int(command[1])
        damage = int(command[2])
        if 0 <= current_index < len(war_ship):
            war_ship[current_index] -= damage
            if war_ship[current_index] <= 0:
                is_down = True
                print(f"You won! The enemy ship has sunken.")
                break

    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < len(pirate_ship):
            if end_index <= len(pirate_ship):
                for state in range(start_index, end_index + 1):
                    pirate_ship[state] -= damage
                    if pirate_ship[state] <= 0:
                        is_down = True
                        print(f"You lost! The pirate ship has sunken.")
                        break

    elif command[0] == "Repair":
        number = int(command[1])
        health = int(command[2])
        if 0 <= number < len(pirate_ship) and health > 0:
            pirate_ship[number] += health
            if pirate_ship[number] > max_health:
                pirate_ship[number] = max_health

    elif command[0] == "Status":
        sections = 0
        for status in pirate_ship:
            if status < max_health / 5:
                sections += 1
        print(f"{sections} sections need repair.")
        continue

pirate = sum(pirate_ship)
warship = sum(war_ship)
if not is_down:
    print(f"Pirate ship status: {pirate}")
    print(f"Warship status: {warship}")
