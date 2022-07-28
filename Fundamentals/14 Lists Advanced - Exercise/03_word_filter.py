# Using comprehension, write a program that receives some text, separated by space,
# and take only those words whose length is even. Print each word on a new line.

words = input().split(' ')
result = [el for el in words if len(el) % 2 == 0]
print('\n'.join(result))
