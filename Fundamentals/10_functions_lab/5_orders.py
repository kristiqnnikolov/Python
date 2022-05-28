# Write a function that calculates the total price of an order and returns it.
# The function should receive one of the following products:
# "coffee", "coke", "water", or "snacks", and a quantity of the product.
# The prices for a single piece of each product are:
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00
#
# Print the result formatted to the second decimal place.


def price(product, quantity):
    if product == 'coffee':
        return quantity * 1.5
    elif product == 'water':
        return quantity * 1
    elif product == 'coke':
        return quantity * 1.4
    elif product == 'snacks':
        return quantity * 2


product = input()
quantity = int(input())

total = price(product, quantity)
print(f"{total:.2f}")
