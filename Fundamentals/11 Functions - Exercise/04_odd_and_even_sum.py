# You will receive a single number. You should write a function that returns the sum of all even and
# all odd digits in a given number. The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

def even_odd(nums):
    even_sum = 0
    odd_sum = 0
    for a in nums:
        if a % 2 == 0:
            even_sum += a
        else:
            odd_sum += a
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


numbers = map(int, list(input()))
even_odd(numbers)
