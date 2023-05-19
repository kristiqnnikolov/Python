# Create a function called even_odd() that can receive a different quantity of numbers and a command at the end.
# The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.
# Submit only the function in the judge system.
def even_odd(*args):
    if args[-1] == 'even':
        return [int(x) for x in args[:-1] if x % 2 == 0]
    elif args[-1] == 'odd':
        return [int(x) for x in args[:-1] if x % 2 == 1]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
