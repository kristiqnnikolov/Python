days = int(input())
players = int(input())
energy = float(input())
water = float(input())
food = float(input())
total_food = days * players * food
total_water = days * players * water
for day in range(1, days + 1):
    day_energy = float(input())
    energy -= day_energy
    if energy <= 0:
        break
    if day % 2 == 0:
        total_water *= 0.7
        energy *= 1.05
        if energy <= 0:
            break
    if day % 3 == 0:
        total_food -= total_food / players
        energy *= 1.1
        if energy <= 0:
            break
if energy > 0:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
