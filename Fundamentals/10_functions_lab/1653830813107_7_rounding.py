# Write a program that rounds all the given numbers, separated by a single space,
# and prints the result as a list. Use round().


def rounding_list(float_list):
    list = []
    for num in float_list:
        list.append(round(float(num)))
    return list


numbers = input().split()
print(rounding_list(numbers))
