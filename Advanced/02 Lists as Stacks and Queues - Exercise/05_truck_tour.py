# You are driving a truck on a circle road with N petrol pumps on it.
# The petrol pumps are numbered 0 to (N−1) (both inclusive).
# For each petrol pump you will receive two pieces of information (separated by a single space):
# -	the amount of petrol that petrol pump will give
# -	the distance from that petrol pump to the next petrol pump (kilometers)
# Initially, you have a tank of infinite capacity carrying no petrol.
# The truck can start the tour at any of the petrol pumps and it will move one kilometer for each liter of the petrol.
# Calculate the first point from where the truck will be able to complete the circle.
# Consider that the truck will stop at each of the petrol pumps.
# Input
# •	On the first line you will receive the number of petrol pumps - N
# •	On the next N-lines you will receive the amount of petrol that petrol pump will give and the distance between that
# petrol pump and the next petrol pump, separated by single space
# Output
# •	An integer which will be the smallest index of a petrol pump from which you can start the tour
from collections import deque

pumps = int(input())
tokens = deque()

for i in range(pumps):
    line = [int(x) for x in input().split()]
    tokens.append(line)

not_passed = True

fuel = 0
starting_pump = 0
while not_passed:
    for pump in tokens:
        if pump == tokens[-1]:
            not_passed = False
            break
        added_fuel, needed_fuel = pump[:]
        if fuel + added_fuel >= needed_fuel:
            fuel += added_fuel
            fuel -= needed_fuel
        else:
            starting_pump += 1
            fuel = 0
            tokens.rotate(-1)
            break

print(starting_pump)
