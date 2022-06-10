# You will receive two lines of input:
# •	a list of employees' happiness as a string of numbers separated by a single space
# •	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# •	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"

def happiness(employees, factor):
    happy = [int(el) * factor for el in employees]
    avg_happiness = sum(happy) / len(happy)
    happy_employees = [x for x in happy if x > avg_happiness]
    half = len(happy) / 2
    if len(happy_employees) >= half:
        return f"Score: {len(happy_employees)}/{len(happy)}. Employees are happy!"
    else:
        return f"Score: {len(happy_employees)}/{len(happy)}. Employees are not happy!"


employees = input().split()
factor = int(input())
print(happiness(employees, factor))
