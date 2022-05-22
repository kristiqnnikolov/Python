# As a young baker, you are baking the bread out of the bakery.
# You have initial energy 100 and initial coins 100. You will be given a string representing the working day events.
# Each event is separated with '|' (vertical bar): "event1|event2| … eventN"
# Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")
# •	If the event is "rest":
# You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100).
# Print: "You gained {gained_energy} energy.".
# After that, print your current energy: "Current energy: {current_energy}.".
# •	If the event is "order":
# You've earned some coins (the number in the second part).
# Each time you get an order, your energy decreases by 30 points.
# 	If you have the energy to complete the order, print: "You earned {earned} coins.".
# 	Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".
# •	In any other case, you have an ingredient you should buy.
# The second part of the event contains the coins you should spend.
# If you have enough money, you should buy the ingredient and print:
# "You bought {ingredient}."
# Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
# If you managed to handle all events through the day, print on the following 3 lines:
# "Day completed!"
# "Coins: {coins}"
# "Energy: {energy}"


events = input().split("|")
energy = 100
coins = 100
loops = len(events)
loop_counter = 0
for event_or_ingredient in events:
    current_event_or_ingredient = event_or_ingredient.split("-")
    types = current_event_or_ingredient[0]
    value = int(current_event_or_ingredient[1])
    if types == 'order':
        if energy >= 30:
            coins += value
            energy -= 30
            print(f"You earned {value} coins.")
            loop_counter += 1
        else:
            energy += 50
            if energy >= 100:
                energy = 100
            print(f"You had to rest!")
            loop_counter += 1
    elif types == 'rest':
        if energy >= 100:
            print(f"You gained {0} energy.")
            print(f"Current energy: {energy}.")
            energy = 100
            loop_counter += 1
            continue
        else:
            energy += value
            print(f"You gained {value} energy.")
            print(f"Current energy: {energy}.")
            loop_counter += 1
            continue
    else:
        if value <= coins:
            coins -= value
            print(f"You bought {types}.")
            loop_counter += 1
        else:
            print(f"Closed! Cannot afford {types}.")
            break
if loops == loop_counter:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
