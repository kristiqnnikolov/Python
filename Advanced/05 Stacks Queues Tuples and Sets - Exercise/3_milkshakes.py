# You are learning how to make milkshakes.
# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start from the last chocolate and try to match it with the first cup of milk.
# If their values are equal, you should make a milkshake and remove both ingredients.
# Otherwise, you should move the cup of milk at the end of the sequence and decrease the value of the chocolate by 5
# You are learning how to make milkshakes.
# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start from the last chocolate and try to match it with the first cup of milk. If their values are equal,
# you should make a milkshake and remove both ingredients. Otherwise, you should move the cup of milk at the end of the
# sequence and decrease the value of the chocolate by 5 without moving it from its position.
# If any of the values are equal to or below 0, you should remove them from the records
# right before mixing them with the other ingredient.
# When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or
# cups of milk left, you need to stop making chocolate milkshakes.
# Input
# •	On the first line of input, you will receive the integers representing the chocolate, separated by  ", ".
# •	On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
# Output
# •	On the first line, print:
# o	If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
# o	Otherwise: "Not enough milkshakes."
# •	On the second line - print:
# o	If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
# o	Otherwise: "Chocolate: empty"
# •	On the third line - print:
# o	If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
# o	Otherwise: "Milk: empty"
from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    chocolate = chocolates.pop()
    milk = cups_of_milk.popleft()

    if chocolate <= 0 and milk <= 0:
        continue

    if chocolate <= 0:
        cups_of_milk.appendleft(milk)
        continue

    if milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        chocolates.append(chocolate - 5)
        cups_of_milk.append(milk)
if milkshakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print('Chocolate: empty')

if cups_of_milk:
    print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
else:
    print("Milk: empty")
