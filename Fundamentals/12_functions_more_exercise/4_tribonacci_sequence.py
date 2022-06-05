# In the Tribonacci sequence, every number is formed by the sum of the previous 3.
# Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space,
# starting from 1. You will receive a positive integer number as input.

def tribonacci(x):
    list = [0, 0, 1]
    for a in range(x - 1):
        list.append(sum(list[-3:]))
    return list[-x:]


integer = int(input())
output = ' '.join([str(x) for x in tribonacci(integer)])

print(output)
