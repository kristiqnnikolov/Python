# Since it is Easter, you have decided to make some loaves of Easter bread and exchange them for eggs.
# Create a program that calculates how many loaves you can make with the budget you have.
#  First, you will receive your budget.
#  Then, you will receive the price for 1 kg flour. Here is the recipe for one bread:
# Eggs	1 pack
# Flour	1 kg
# Milk	0.250 l
# The price for 1 pack of eggs is 75% of the price for 1 kg flour.
# The price for 1l milk is 25% more than the price for 1 kg flour.
# Notice that you need 0.250l milk for one bread, and the calculated price is for 1l.
# Start cooking the loaves and keep making them until you have enough budget. Keep in mind that:
# •	For every bread that you make, you will receive 3 colored eggs.
# •	For every 3rd bread you make, you will lose some of your colored eggs after receiving the usual 3 colored eggs
# for your bread. The count of eggs you will lose is calculated when you subtract 2
# from your current count of loaves – ({current_bread_count} – 2)
# In the end, print the loaves of bread you made, the eggs you have gathered, and the money you have left,
# formatted to the 2nd decimal place, in the following format:
# "You made {number_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."


budget = float(input())
price_flour = float(input())

for_one_bread = price_flour + (price_flour * 0.75) + ((price_flour * 1.25) / 4)
number_bread = 0
colored_eggs = 0

while budget > for_one_bread:
    budget -= for_one_bread
    number_bread += 1
    colored_eggs += 3
    if number_bread % 3 == 0:
        deduction = number_bread - 2
        colored_eggs -= deduction
money_left = abs(budget)
print(
    f"You made {number_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
