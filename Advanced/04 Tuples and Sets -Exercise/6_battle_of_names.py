# You will receive a number N. On the next N lines, you will be receiving names.
# You must sum the ascii values of each letter in the name and integer divide it to the number of the current row
# (starting from 1). Save the result to a set of either odd or even numbers,
# depending on if the devised number is an odd or even. After that, sum the values of each set.
# •	If the sums of the two sets are equal, print the union of the values, separated by ", ".
# •	If the sum of the odd numbers is bigger than the sum of the even numbers,
# print the different values, separated by ", ".
# •	If the sum of the even numbers is bigger than the sum of the odd numbers,
# print the symmetric different values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set
from math import floor

odd = set()
even = set()

for row in range(1, int(input()) + 1, 1):
    name = input()
    points = 0
    for x in name:
        points += ord(x)
    points /= row
    points = floor(points)
    if points % 2 == 0:
        even.add(points)
    else:
        odd.add(points)

sum_odd = sum(odd)
sum_even = sum(even)

if sum_odd > sum_even:
    result = [str(x) for x in odd.difference(even)]
    print(f'{", ".join(result)}')
elif sum_odd < sum_even:
    result = [str(x) for x in even.symmetric_difference(odd)]
    print(f'{", ".join(result)}')
else:
    result = [str(x) for x in even.union(odd)]
    print(f'{", ".join(result)}')