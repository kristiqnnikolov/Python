# Write a program that prints you a receipt for your new computer.
# You will receive the parts' prices (without tax) until you receive what type of customer this is - special or regular.
# Once you receive the type of customer you should print the receipt.
# The taxes are 20% of each part's price you receive.
# If the customer is special, he has a 10% discount on the total price with taxes.
# If a given price is not a positive number,
# you should print "Invalid price!" on the console and continue with the next price.
# If the total price is equal to zero, you should print "Invalid order!" on the console.

total = 0.0
taxes = 0.0
with_taxes = 0.0

while True:
    price = input()
    if price == 'special' or price == 'regular':
        if total == 0:
            print(f"Invalid order!")
            break
    elif float(price) < 0:
        print(f"Invalid price!")
        continue
    if price == 'special':
        with_taxes += total * 1.2
        taxes += with_taxes - total
        with_taxes *= 0.9
        break
    elif price == 'regular':
        with_taxes += total * 1.2
        taxes += with_taxes - total
        break
    else:
        total += float(price)

if taxes > 0:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    print(f"Total price: {with_taxes:.2f}$")
