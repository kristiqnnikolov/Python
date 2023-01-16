# Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones.
# On the first line, you will receive an integer N. On the next N lines, you will receive a username.
# Print the collection on the console (the order does not matter):

all_names = set()

for none in range(int(input())):
    name = input()
    all_names.add(name)
print('\n'.join(all_names))