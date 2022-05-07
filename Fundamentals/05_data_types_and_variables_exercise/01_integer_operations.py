# Write a program that reads four integer numbers.
# It should add the first to the second number, integer divide the sum by the third number,
# and multiply the result by the fourth number. Print the final result.


from math import floor

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = floor((a + b) / c)
f = floor(e * d)
print(f"{f:.0f}")
