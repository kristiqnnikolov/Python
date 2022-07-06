# Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons.
# The input holds two lines: the number of people N and the capacity P of the elevator.


import math

n = int(input())
p = int(input())
z = (n / p)
print(f"{math.ceil(z)}")
