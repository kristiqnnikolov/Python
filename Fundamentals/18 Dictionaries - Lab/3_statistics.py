# You seem to be doing great at your first job, so your boss decides to give you as your next task something more
# challenging. You have to accept all the new products coming in the bakery and finally gather some statistics.
# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics".
# Sometimes you may receive a product more than once.
# In that case, you have to add the new quantity to the existing one.
# When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"

current_command = input()
products = {}
while current_command != 'statistics':
    command = current_command.split(": ")
    product = command[0]
    value = int(command[1])
    if product not in products:
        products[product] = value
    else:
        products[product] += value
    current_command = input()

print(f"Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
