# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end".
# You should register each user into the corresponding course. If the given course does not exist, add it.
# When you receive the command "end", print the courses with their names and total registered users.
# For each course, print the registered users.

command = input()
softuni = {}
while command != 'end':
    courses = command.split(" : ")
    course = courses[0]
    names = courses[1]
    if course not in softuni:
        softuni[course] = []
    softuni[course].append(names)
    command = input()
for key, value in softuni.items():
    print(f'{key}: {len(value)}')
    name = [f' -- {x}' for x in value]
    print(*name, sep="\n")
