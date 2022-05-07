# As a gladiator, Peter needs to repair his broken equipment when he loses a fight.
# His equipment consists of a helmet, a sword, a shield, and an armor.
# You will receive Peter's lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment.
# Calculate his expenses for the year for renewing his equipment.


lost_fights = int(input())
price_helm = float(input())
price_sword = float(input())
price_shield = float(input())
price_armor = float(input())
expenses = 0
second_time = 0

for battle in range(1, lost_fights + 1):
    if battle % 2 == 0:
        expenses += price_helm
    if battle % 3 == 0:
        expenses += price_sword
    if battle % 2 == 0 and battle % 3 == 0:
        expenses += price_shield
        second_time += 1
        if second_time == 2:
            expenses += price_armor
            second_time = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")
