# Write a program that receives a sequence of numbers, separated by a single space,
# and prints their absolute value as a list. Use abs().

list = input().split()
new = []
for num in list:
    new.append(abs(float(num)))
print(new)
