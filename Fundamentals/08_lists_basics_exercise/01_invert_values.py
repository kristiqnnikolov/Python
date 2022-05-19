# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.

str = input()
numbers = str.split()
opposites = []
for i in numbers:
    i = int(i)
    if i > 0:
        z = i - i - i
        opposites.append(z)
    else:
        z = i - i - i
        opposites.append(z)
print(opposites)
