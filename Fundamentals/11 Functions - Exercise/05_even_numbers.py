# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().


def check(numbers):
    if numbers % 2 == 0:
        return True
    return False


inputt = filter(check, list(map(int, input().split(" "))))
print(list(inputt))
