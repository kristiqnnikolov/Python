# Write a function that receives a string and a counter n.
# The function should return a new string – the result of repeating the old string n times.
# Print the result of the function. Try using lambda.

string = input()
number = int(input())

repeat = lambda a, b: a * b
result = repeat(string, number)
print(result)
