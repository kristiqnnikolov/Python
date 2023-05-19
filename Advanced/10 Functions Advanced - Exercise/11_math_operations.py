# Write a function named math_operations that receives a different number of floats as arguments and 4 keyword arguments
# The keys will be single letters: "a", "s", "d", "m", and the values will be numbers.
# You need to take each float argument from the sequence and do mathematical operations as follows:
# •	The first element should be added to the value of the key "a"
# •	The second element should be subtracted from the value of the key "s"
# •	The third element should be divisor to the value of the key "d"
# •	The fourth element should be multiplied by the value of the key "m"
# •	Each result should replace the value of the corresponding key
# •	You must repeat the same steps consecutively until you run out of numbers
# Beware: You cannot divide by 0. If the operation could throw an error,
# you should skip the operation and continue to the next one.
# After you finish calculating all numbers, sort the four elements by their values in descending order.
# If two or more values are equal, sort them by their keys in ascending order (alphabetically).
# In the end, return each key-value pair in the format "{key}: {value}" on separate lines.
# Each value should be formatted to the first decimal point.
# For more clarifications, see the examples below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input. Just parameters passed to your function.
# •	All of the given numbers will be valid integers in the range [-100, 100]
# Output
# •	The function should return the final dictionary
def math_operations(*args, **kwargs):
    numbers = [float(x) for x in args]
    dict = {}
    dict["a"] = kwargs.get("a")
    dict["d"] = kwargs.get("d")
    dict["m"] = kwargs.get("m")
    dict["s"] = kwargs.get("s")
    for x in range(0, len(numbers), 4):
        dict["a"] += numbers[x]
    for x in range(1, len(numbers), 4):
        dict["s"] -= numbers[x]
    for x in range(2, len(numbers), 4):
        if numbers[x] == 0:
            continue
        dict["d"] /= numbers[x]
    for x in range(3, len(numbers), 4):
        dict["m"] *= numbers[x]
    result = ""
    for key, value in sorted(dict.items(), key=lambda kvpt: -kvpt[1]):
        result += f"{key}: {value:.1f}"'\n'
    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
