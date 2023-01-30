# First, you will be given two sequences of integers values on different lines.
# The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
# •	"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
# •	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
# •	"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
# •	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
# •	"Check Subset" - check if any of the given sequences are a subset of the other.
# If it is, print "True". Otherwise, print "False".
# In the end, print the final sequences, separated by a comma and a space ", ".
# The values in each sequence should be sorted in ascending order.

one = set(int(x) for x in input().split())
two = set(int(x) for x in input().split())
number = int(input())

for none in range(number):
    command = input().split()
    if len(command) > 2:
        numbers = [int(x) for x in set(command[2:])]

        if command[0] == 'Add' and command[1] == 'First':
            one = one.union(numbers)
        elif command[0] == 'Add' and command[1] == 'Second':
            two = two.union(numbers)

        elif command[0] == 'Remove' and command[1] == 'First':
            for i in numbers:
                if i in one:
                    one.discard(i)
        elif command[0] == 'Remove' and command[1] == 'Second':
            for i in numbers:
                if i in two:
                    two.discard(i)
    else:
        if one.issubset(two) or two.issubset(one):
            print("True")
        else:
            print("False")

print(*sorted(one), sep=', ')
print(*sorted(two), sep=', ')
