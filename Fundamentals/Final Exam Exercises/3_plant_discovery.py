# You have now returned from your world tour.
# On your way, you have discovered some new plants, and you want to gather some information about
# them and create an exhibition to see which plant is highest rated.
# On the first line, you will receive a number n. On the next n lines,
# you will be given some information about the plants that you have discovered in the format:
# "{plant}<->{rarity}". Store that information because you will need it later.
# If you receive a plant more than once, update its rarity.
# After that, until you receive the command "Exhibition", you will be given some of these commands:
# •	"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
# •	"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
# •	"Reset: {plant}" – remove all the ratings of the given plant
# Note: If any given plant name is invalid, print "error"
# After the command "Exhibition", print the information that you have about the plants in the following format:
# "Plants for the exhibition:
# - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
# …
# - {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
# The average rating should be formatted to the second decimal place.

lines = int(input())

plants = {}
for info in range(lines):
    plant_rarity = input().split("<->")
    plant = plant_rarity[0]
    rarity = int(plant_rarity[1])
    if plant not in plants:
        plants[plant] = {"rarity": rarity, "rating": []}
current_command = input()
while not current_command == 'Exhibition':
    command = current_command.split(": ")
    action = command[0]
    if action == 'Rate':
        plant_rating = command[1].split(" - ")
        plant = plant_rating[0]
        rating = int(plant_rating[1])
        if plant in plants:
            plants[plant]["rating"].append(rating)
        else:
            print("error")
    elif action == 'Update':
        plant_rating = command[1].split(" - ")
        plant = plant_rating[0]
        rarity = int(plant_rating[1])
        if plant in plants:
            plants[plant]["rarity"] = rarity
        else:
            print("error")
    elif action == 'Reset':
        plant = command[1]
        if plant in plants:
            plants[plant]["rating"] = []
        else:
            print("error")

    current_command = input()
print("Plants for the exhibition:")
for plant, rarity_rating in plants.items():
    if len(rarity_rating['rating']) > 0:
        rating = sum(rarity_rating['rating']) / len(rarity_rating["rating"])
    else:
        rating = 0
    print(f"- {plant}; Rarity: {rarity_rating['rarity']}; Rating: {rating:.2f}")
