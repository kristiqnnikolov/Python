# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers.

def even(num):
    nums = [int(x) for x in num]
    filtered = [index for index in range(len(nums)) if nums[index] % 2 == 0]
    return filtered


numbers = input().split(", ")
print(even(numbers))
