# Write a program that keeps the information about products and their prices.
# Each product has a name, a price, and a quantity:
# •	If the product doesn't exist yet, add it with its starting quantity.
# •	If you receive a product, which already exists, increases its quantity by the input quantity and if
# its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines.
# Until you receive the command "buy", keep adding items.
# Finally, print all items with their names and the total price of each product.
# Input
# •	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# •	The product data is always delimited by a single space.

command = input()
storage = {}
while command != 'buy':
    products = command.split()
    item = products[0]
    price = products[1]
    quantity = products[2]
    if item not in storage:
        storage[item] = {'price': float(price), 'quantity': int(quantity)}
    else:
        storage[item]['price'] = float(price)
        storage[item]['quantity'] += int(quantity)
    command = input()
for key, value in storage.items():
    total = value['price'] * value['quantity']
    print(f'{key} -> {total:.2f}')
