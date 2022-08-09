# You will be receiving names of students, their ID, and a course of programming they have taken in the format
# "{name}:{ID}:{course}". On the last line, you will receive a name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course in the format:
# "{name} - {ID}" on separate lines.
# Note: each student's ID will always be unique

current_command = input()
my_dict = {}
course_list = []
while current_command != 'programming_basics' or current_command != '2 Fundamentals':
    command = current_command.split(":")
    if len(command) == 1:
        break
    name = command[0]
    id = command[1]
    course = command[2].split()
    if name not in my_dict:
        course_list.append(id)
        course_list.append(course)
        my_dict[name] = course_list
        course_list = []
    current_command = input()
for key, value in my_dict.items():
    if current_command.split("_") in value:
        print(f"{key} - {value[0]}")
