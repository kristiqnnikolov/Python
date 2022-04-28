# Write a program that reads an integer n.
# Then, for all numbers in the range [1, n], prints the number and if it is special or not (True / False).
# A number is special when the sum of its digits is 5, 7, or 11.


number = int(input())
for n in range(1, number + 1):
    working_number = str(n)
    digit_sum = 0
    for num in working_number:
        digit_sum += int(num)
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f'{n} -> True')
    else:
        print(f'{n} -> False')
