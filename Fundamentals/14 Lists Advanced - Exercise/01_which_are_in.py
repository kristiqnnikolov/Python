# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line,
# which are substrings of any string in the second input line.

words = input().split(", ")
letters = input()
new_list = [x for x in words if x in letters]
print(new_list)
