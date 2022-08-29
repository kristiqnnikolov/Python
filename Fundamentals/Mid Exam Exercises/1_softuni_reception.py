# Every day, thousands of students pass by the reception at SoftUni with different questions to ask.
# The employees have to help everyone by providing all the information and answering all of the questions.
# Three employees are working on the reception all day. Each of them can handle a different number of students per hour.
# Your task is to calculate how much time it will take to answer all the questions of a given number of students.
# First, you will receive 3 lines with integers,
# representing the number of students that each employee can help per hour.
# On the following line, you will receive students count as a single integer.
# Every fourth hour, all employees have a break, so they don't work for an hour.
# It is the only break for the employees, because they don't need rest, nor have a personal life.
# Calculate the time needed to answer all the student's questions and print it in the following format:
# "Time needed: {time}h."

employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
students = int(input())
hours = 0
while students > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    students -= employee_one
    students -= employee_two
    students -= employee_three

    if students <= 0:
        break

print(f"Time needed: {hours}h.")
