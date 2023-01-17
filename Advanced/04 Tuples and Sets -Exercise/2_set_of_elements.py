# Write a program which prints a set of elements. On the first line, you will receive two numbers - n and m,
# separated by a single space - they represent the lengths of two separate sets.
# On the next n + m lines you will receive n numbers, which are the numbers in the first set, and m numbers,
# which are in the second set. Find all the unique elements that appear in both and print
# them on separate lines (the order does not matter).
# For example:
# Set with length n = 4: {1, 3, 5, 7}
# Set with length m = 3: {3, 4, 5}
# Set that contains all the elements that repeat in both sets -> {3, 5}

n_m = input().split()

n_set = set()
m_set = set()

loops = sum([int(x) for x in n_m])
for none in range(int(n_m[0])):
    number = input()
    n_set.add(number)
for none in range(int(n_m[1])):
    number = input()
    m_set.add(number)

result = n_set.intersection(m_set)
print("\n".join(sorted(result)))
