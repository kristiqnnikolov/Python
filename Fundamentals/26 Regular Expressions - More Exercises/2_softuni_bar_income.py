# Let`s take a break and visit the game bar at SoftUni.
# It is about time for the people behind the bar to go home and you are the person who has to draw the line and
# calculate the money from the products that were sold throughout the day.
# Until you receive a line with text "end of shift" you will be given lines of input.
# But before processing that line you should do some validations first.
# Each valid order should have a customer, product, count and a price:
# •	Valid customer's name should be surrounded by '%' and must start with a capital letter,
# followed by lower-case letters
# •	Valid product contains any word character (not only letters) and must be surrounded by '<' and '>'
# •	Valid count is an integer, surrounded by '|'
# •	Valid price is any real number followed by '$'
# The parts of a valid order should appear in the order given: customer, product, count and a price.
# Between each part there can be other symbols, except ('|', '$', '%' and '.')
# For each valid line print on the console: "{customerName}: {product} - {totalPrice}"
# When you receive "end of shift" print the total amount of money for the day rounded
# to 2 decimal places in the following format: "Total income: {income}".

import re

command = input()

regex = r"^%([A-Z][a-z]+)%(?:[^\.\|\$%]+)?<(\w+)>(?:[^\.\|\$%]+)?\|(\d+)\|(?:[^\.\|\$%]+)?((?<=\D)\d+(?:\.\d+)?)(?=\$)\$$"
all_total = 0
while not command == 'end of shift':
    matches = re.findall(regex, command)
    for match in matches:
        name = match[0]
        product = match[1]
        total = float(match[2]) * float(match[3])
        all_total += total
        print(f'{name}: {product} - {total:.2f}')
    command = input()
print(f'Total income: {all_total:.2f}')
