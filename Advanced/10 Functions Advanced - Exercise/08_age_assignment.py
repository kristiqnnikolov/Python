# Create a function called age_assignment() that receives a different number of names and a
# different number of key-value pairs. The key will be a single letter (the first letter of each name) and the value
# - a number (age). Find its first letter in the key-value pairs for each name and assign the age to the person's name.
# Then, sort the names in ascending order (alphabetically) and return the information
# for each person on a new line in the format: "{name} is {age} years old."
# Submit only the function in the judge system.
def age_assignment(*args, **kwargs):
    result = {}
    final = ""
    for x in args:
        if x[0] in kwargs:
            result[x] = kwargs.get(x[0])
    for name, age in sorted(result.items()):
        final += f"{name} is {age} years old."'\n'
    return final


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
