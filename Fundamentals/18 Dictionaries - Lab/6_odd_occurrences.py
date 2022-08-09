# Write a program that extracts all elements from a given sequence of words present in
# it an odd number of times (case-insensitive).
# •	Words are given on a single line, space-separated.
# •	Print the result elements in lowercase, in their order of appearance.


data = input().lower()
data = data.split()
my_dict = {}
for value in data:
    if value not in my_dict:
        my_dict[value] = 1
    else:
        my_dict[value] += 1
for key, value in my_dict.items():
    if value % 2 != 0:
        print(key, end=' ')
