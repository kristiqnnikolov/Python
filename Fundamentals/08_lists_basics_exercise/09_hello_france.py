# You want to go to France by train, and the train ticket costs exactly 150$.
# You do not have enough money,
# so you decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type	Maximum Price
# Clothes	50.00
# Shoes	35.00
# Accessories	20.50
# If a price for a particular item is higher than the maximum price, don't buy it.
# Every time you buy an item, you have to reduce the budget with its price value.
# If you don't have enough money for it, you can't buy it. Buy as many items as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it.
# Calculate if the budget after selling all the items is enough for buying the train ticket.


items = input().split("|")
budget = float(input())
list_of_items = []
train_ticket = 150
profit = 0
profit_list = []
start_money = budget
for symbol in items:
    strings = symbol.replace("->", " = ")
    list_of_items.append(strings)
for kind in list_of_items:
    current_kind = kind.split(" = ")
    type_of_items = current_kind[0]
    item_value = float(current_kind[1])
    if type_of_items == 'Clothes':
        if not item_value > 50:
            if budget >= item_value:
                budget -= item_value
                single_profit = item_value * 1.4
                profit += single_profit
                profit_list.append(f"{single_profit:.2f}")
    elif type_of_items == 'Shoes':
        if not item_value > 35:
            if budget >= item_value:
                budget -= item_value
                single_profit = item_value * 1.4
                profit += single_profit
                profit_list.append(f"{single_profit:.2f}")
    elif type_of_items == 'Accessories':
        if not item_value > 20.50:
            if budget >= item_value:
                budget -= item_value
                single_profit = item_value * 1.4
                profit += single_profit
                profit_list.append(f"{single_profit:.2f}")
total = budget + profit
after = total - start_money
print(*profit_list, sep=" ")
print(f"Profit: {after:.2f}")
if total >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
