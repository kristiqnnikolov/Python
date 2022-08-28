# Your first task is to determine if the given sequence of characters is a valid barcode or not.
# Each line must not contain anything else but a valid barcode. A barcode is valid when:
# •	It is surrounded by a "@" followed by one or more "#"
# •	It is at least 6 characters long (without the surrounding "@" or "#")
# •	It starts with a capital letter
# •	It contains only letters (lower and upper case) and digits
# •	It ends with a capital letter
# Examples of valid barcodes: @###Che46sE@##, @#FreshFisH@#, @###Brea0D@###, @##Che46sE@##
# Examples of invalid barcodes: ##InvaliDiteM##, @InvalidIteM@, @#Invalid_IteM@#
# Next, you have to determine the product group of the item from the barcode.
# The product group is obtained by concatenating all the digits found in the barcode.
# If there are no digits present in the barcode, the default product group is "00".
# Examples:
# @#FreshFisH@# -> product group: 00
# @###Brea0D@### -> product group: 0
# @##Che4s6E@## -> product group: 46

import re

lines = int(input())
regex = r"(@(#+)([A-Z]{1}[a-zA-Z0-9]{4,}[A-Z]{1})@(#+))"
for x in range(lines):
    barcode = input()
    matches = re.findall(regex, barcode)
    index = ""
    if not matches == []:
        for match in matches[0]:
            for i in match:
                if i.isdigit():
                    index += i
                    continue
            if not index == "":
                print(f"Product group: {index}")
            else:
                print(f"Product group: 00")
            break

    else:
        print("Invalid barcode")
