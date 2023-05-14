# Write a program to flatten several lists of numbers received in the following format:
# 	String with numbers or empty strings separated by "|"
# 	Values are separated by spaces (" ", one or several)
# 	Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below
line = [x for x in input().split("|")]
result = []
for current in reversed(line):
    nums = current.split()
    for x in nums:
        result.append(x)
print(*result)
