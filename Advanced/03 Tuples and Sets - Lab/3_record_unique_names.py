# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.

all_names = set()

for none in range(int(input())):
    name = input()
    all_names.add(name)
print('\n'.join(all_names))
