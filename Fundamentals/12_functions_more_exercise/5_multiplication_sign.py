# You will receive three integer numbers.
# Write a program that finds if their multiplication (the result) is negative, positive, or zero.
# Try to do this WITHOUT multiplying the 3 numbers.

def negative_or_positive(a, b, c):
    if a > 0 and b < 0 and c < 0:
        return f'positive'
    elif a < 0 and b < 0 and c > 0:
        return f'positive'
    elif a < 0 and b > 0 and c < 0:
        return f'positive'
    elif a > 0 and b > 0 and c > 0:
        return f'positive'
    elif a == 0 or b == 0 or c == 0:
        return f'zero'
    else:
        return f'negative'


a = int(input())
b = int(input())
c = int(input())
print(negative_or_positive(a, b, c, ))
