# Maria wants to make a firework show for the wedding of her best friend.
# We should help her to make the perfect firework show.
#
# First, you will be given a sequence of integers representing firework effects. Afterwards you will be given another sequence of integers representing explosive power.
# You need to start from the first firework effect and try to mix it with the last explosive power.
# If the sum of their values is:
# •	divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
# •	divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
# •	divisible by both 3 and 5 – create Crossette firework and remove both materials
# Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence.
# Then, try to mix the same explosive power with the next firework effect.
# If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other.
# When you have successfully prepared enough fireworks for the show or you have no more
# firework punches or explosive power, you need to stop mixing.
# To make the perfect firework show, Maria needs 3 of each of the firework types.
# Input
# •	On the first line, you will receive the integers representing the firework effects, separated by ", ".
# •	On the second line, you will receive the integers representing the explosive power, separated by ", ".
# Output
# •	On the first line, print:
# o	if Maria successfully prepared the firework show: "Congrats! You made the perfect firework show!"
# o	if Maria failed to prepare it: "Sorry. You can't make the perfect firework show."
# •	On the second line, print all firework effects left if there are any:
# o	"Firework Effects left: {effect1}, {effect2}, (…)"
# •	On the third line, print all explosive fillings left if there are any:
# o	" Explosive Power left: {filling1}, {filling2}, (…)"
# •	Then, you need to print all fireworks and the amount you have of them:
# o	"Palm Fireworks: {count}"
# o	"Willow Fireworks: {count}"
# o	"Crossette Fireworks: {count}"
from collections import deque

firework_effect = deque([int(x) for x in input().split(', ')])
explosive_power = deque([int(x) for x in input().split(', ')])

palm = 0
willow = 0
crossette = 0
perfect_firework_show = False

while firework_effect and explosive_power:
    current_effect = firework_effect.popleft()
    current_power = explosive_power.pop()
    if current_effect > 0 and current_power > 0:
        total = current_effect + current_power
    else:
        if current_power > 0:
            explosive_power.append(current_power)
        if current_effect > 0:
            firework_effect.appendleft(current_effect)
        continue
    if total % 3 == 0 and not total % 5 == 0:
        palm += 1
    elif total % 5 == 0 and not total % 3 == 0:
        willow += 1
    elif total % 3 == 0 and total % 5 == 0:
        crossette += 1
    else:
        firework_effect.append(current_effect - 1)
        explosive_power.append(current_power)
    if palm >= 3 and willow >= 3 and crossette >= 3:
        perfect_firework_show = True
        break

if perfect_firework_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effect:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effect])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")
print(f'Palm Fireworks: {palm}')
print(f'Willow Fireworks: {willow}')
print(f'Crossette Fireworks: {crossette}')
