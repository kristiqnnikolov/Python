# Tony and Andi love playing in the snow and having snowball fights,
# but they always argue about which makes the best snowballs.
# They have decided to involve you in their fray by writing a program
# that calculates snowball data and outputs the best snowball value.
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
# •	The weight of the snowball (integer).
# •	The time needed for the snowball to get to its target (integer).
# •	The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.

number_of_snowballs = int(input())
highest = 0
current_formula = 0
is_highest = False
highest_time = 0
highest_weight = 0
highest_quality = 0

for snowballs in range(1, number_of_snowballs + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    formula = (weight / time) ** quality
    current_formula = formula
    if current_formula > highest:
        highest = current_formula
        is_highest = True
        highest_quality = quality
        highest_time = time
        highest_weight = weight
if is_highest:
    print(f"{highest_weight} : {highest_time} = {highest:.0f} ({highest_quality})")
