# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ",
# and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number

words = list(map(int, input().split(',')))

positive = [str(el) for el in words if el >= 0]
negative = [str(el) for el in words if el < 0]
even = [str(el) for el in words if el % 2 == 0]
odd = [str(el) for el in words if el % 2 != 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
