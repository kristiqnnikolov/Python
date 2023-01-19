# Write a program that keeps all the unique chemical elements.
# On the first line you will be given a number n - the count of input lines that you are going to receive.
# On the next n lines, you will be receiving chemical compounds, separated by a single space.
# Your task is to print all the unique ones on separate lines (the order does not matter):

all_chemichals = set()

for none in range(int(input())):
    chemicals = input().split()
    if len(chemicals) > 1:
        for x in range(len(chemicals)):
            all_chemichals.add(chemicals[x])
    else:
        all_chemichals.add(chemicals[0])

print("\n".join(sorted(all_chemichals)))
