# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

def factorial(n):
    return 1 if n == 0 or n == 1 else n * (factorial(n - 1))


number = int(input())
divider = int(input())
result = factorial(number) / factorial(divider)
print(f'{result:.2f}')
