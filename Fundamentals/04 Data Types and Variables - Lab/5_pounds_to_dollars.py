# Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.
# 1 British Pound = 1.31 Dollars.

pounds = float(input())
usd = pounds * 1.31
print(f"{usd:.3f}")
