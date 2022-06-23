# On the first line, you will be given a positive number, which will serve as a divisor.
# On the second line, you will receive a positive number that will be the boundary.
# You should find the largest integer N, that is:
# •	 divisible by the given divisor
# •	  less than or equal to the given bound
# •	 greater than 0
# Note: it is guaranteed that N is found.


import sys

divisor = int(input())
bound = int(input())

max = -sys.maxsize

for x in range(bound + 1):
    if bound >= x > 0:
        if x % divisor == 0:
            max = x
print(max)
