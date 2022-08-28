# Anno 1681. The Caribbean. The golden age of piracy. You are a well-known pirate captain by the name of Jack Daniels.
# Together with your comrades Jim (Beam) and Johnny (Walker), you have been roaming the seas,
# looking for gold and treasure… and the occasional killing, of course.
# Go ahead, target some wealthy settlements and show them the pirate's way!
# Until the "Sail" command is given, you will be receiving:
# •	You and your crew have targeted cities, with their population and gold, separated by "||".
# •	If you receive a city that has already been received,
# you have to increase the population and gold with the given values.
# After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given.
# Events will be in the following format:
# •	"Plunder=>{town}=>{people}=>{gold}"
# o	You have successfully attacked and plundered the town,
# killing the given number of people and stealing the respective amount of gold.
# o	For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
# o	If any of those two values (population or gold) reaches zero, the town is disbanded.
# 	You need to remove it from your collection of targeted cities and print the following message:
# "{town} has been wiped off the map!"
# o	There will be no case of receiving more people or gold than there is in the city.
# •	"Prosper=>{town}=>{gold}"
# o	There has been dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
# o	The gold amount can be a negative number, so be careful.
# If a negative amount of gold is given, print: "Gold added cannot be a negative number!" and ignore the command.
# o	If the given gold is a valid amount,
# increase the town's gold reserves by the respective amount and print the following message:
# "{gold added} gold added to the city treasury. {town} now has {total gold} gold."

command = input()
cities = {}
while not command == 'Sail':
    commands = command.split("||")
    city = commands[0]
    population = int(commands[1])
    gold = int(commands[2])
    if city in cities:
        cities[city]["population"] += population
        cities[city]["gold"] += gold
    else:
        cities[city] = {"population": population, "gold": gold}

    command = input()

text = input()
while not text == 'End':
    txt = text.split("=>")
    action = txt[0]
    town = txt[1]
    if action == 'Plunder':
        people = int(txt[2])
        gold = int(txt[3])
        if town in cities:
            if cities[town]["population"] <= people \
                    or cities[town]["gold"] <= gold:
                del cities[town]
                print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
                print(f"{town} has been wiped off the map!")
            else:
                cities[town]["population"] -= people
                cities[town]["gold"] -= gold
                print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    elif action == 'Prosper':
        town = txt[1]
        gold = int(txt[2])
        if gold >= 0:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")

    text = input()
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
for city, value in cities.items():
    print(f"{city} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
