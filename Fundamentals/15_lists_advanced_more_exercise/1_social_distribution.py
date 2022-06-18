# A core idea of several left-wing ideologies is that the wealthiest should support the poorest,
# no matter what, and that is exactly what you are called to do for this problem.
# On the first line, you will be given the population (numbers separated by comma and space ", ").
# the second line, you will be given the minimum wealth.
# You should distribute the wealth so that no part of the population has less than the minimum wealth.
# To do that, you should always take wealth from the wealthiest part of the population.
# There will be cases where the distribution will not be possible.
# In that case, print: "No equal distribution possible".

numbers = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())

for i in range(len(numbers)):
    if numbers[i] < minimum_wealth:
        a = minimum_wealth - numbers[i]
        max_number = max(numbers)
        if max_number - a >= minimum_wealth:
            numbers[numbers.index(max_number)] -= a
            numbers[i] += a
if sum(numbers) >= len(numbers) * minimum_wealth:
    print(numbers)
else:
    print("No equal distribution possible")
