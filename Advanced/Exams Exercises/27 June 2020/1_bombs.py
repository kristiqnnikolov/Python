# Ezio is still learning how to make bombs. With their help, he will save civilization. We should help Ezio to make his perfect bombs.
#
# You will be given two sequences of integers, representing bomb effects and bomb casings.
# You need to start from the first bomb effect and try to mix it with the last bomb casing.
# If the sum of their values is equal to any of the materials in the table below –
# create the bomb corresponding to the value and remove both bomb materials.
# Otherwise, just decrease the value of the bomb casing by 5. You need to stop combining when you have no more bomb
# effects or bomb casings, or you successfully filled the bombs pouch.
# Bombs:
# •	Datura Bombs: 40
# •	Cherry Bombs: 60
# •	Smoke Decoy Bombs: 120
# To fill the bomb pouch, Ezio needs three of each of the bomb types.
# Input
# •	On the first line, you will receive the integers representing the bomb effects, separated by ", ".
# •	On the second line, you will receive the integers representing the bomb casings, separated by ", ".
# Output
# •	On the first line, print:
# o	if Ezio succeeded to fulfill the bomb pouch: "Bene! You have successfully filled the bomb pouch!"
# o	if Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill the bomb pouch."
# •	On the second line, print all bomb effects left:
# o	If there are no bomb effects: "Bomb Effects: empty"
# o	If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"
# •	On the third line, print all bomb casings left:
# o	If there are no bomb casings: "Bomb Casings: empty"
# o	If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"
# •	Then, you need to print all bombs and the count you have of them, ordered alphabetically:
# o	"Cherry Bombs: {count}"
# o	"Datura Bombs: {count}"
# o	"Smoke Decoy Bombs: {count}"
from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

cherry_bombs = 0
datura_bombs = 0
smoke_decoy_bombs = 0
all_collected = False

while bomb_effects and bomb_casings:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()
    total = current_casing + current_effect
    if total == 40:
        datura_bombs += 1
    elif total == 60:
        cherry_bombs += 1
    elif total == 120:
        smoke_decoy_bombs += 1
    else:
        bomb_effects.appendleft(current_effect)
        bomb_casings.append(current_casing - 5)
    if cherry_bombs >= 3 and datura_bombs >= 3 and smoke_decoy_bombs >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        all_collected = True
        break

if not all_collected:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")
print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")
