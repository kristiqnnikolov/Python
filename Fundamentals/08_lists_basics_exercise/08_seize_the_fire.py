# The group of adventurists has gone on their first task. Now they should walk through fire - literally.
# They should use all the water they have left. Your task is to help them survive.
# Create a program that calculates the water needed to put out a "fire cell",
# based on the given information about its "fire level" and how much it gets affected by water.
# First, you will be given the level of fire inside the cell with the integer value of the cell,
# which represents the needed water to put out the fire.  They will be given in the following format:
# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} = {valueOfCell}"
# Afterward you will receive the amount of water you have for putting out the fires.
# There is a range of fire for each fire type, and if a cell's value is below or exceeds it, it is invalid,
# and you do not need to put it out.
# Type of Fire	Range
# High	81 - 125
# Medium	51 - 80
# Low	1 - 50
# If a cell is valid, you should put it out by reducing the water with its value.
# Putting out fire also takes effort, and you need to calculate it. Its value is equal to 25% of the cell's value.
# In the end, you will have to print the total effort. Keep putting out cells until you run out of water.
# Skip it and try the next one if you do not have enough water to put out a given cell.
# In the end, print the cells you have put out in the following format:
# "Cells:
#  - {cell1}
#  - {cell2}
#  …
#  - {cellN}"
# "Effort: {effort}"
# The effort should be formatted to the second decimal place.
# In the end, print the total fire you have put out from all the cells in the following format:
# "Total Fire: {total_fire}"


all_fires = input().split('#')
water = int(input())
effort = 0
total_fire = 0
cell_values = []
for fire in all_fires:
    current_fire = fire.split(" = ")
    type_of_fire = current_fire[0]
    cell_value = int(current_fire[1])
    if type_of_fire == 'High':
        if not 81 <= cell_value <= 125:
            continue
    elif type_of_fire == 'Medium':
        if not 51 <= cell_value <= 80:
            continue
    elif type_of_fire == 'Low':
        if not 1 <= cell_value <= 50:
            continue
    if water < cell_value:
        continue
    cell_values.append(cell_value)
    water -= cell_value
    effort += cell_value * 0.25
    total_fire += cell_value
print("Cells:")
for cell in cell_values:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
