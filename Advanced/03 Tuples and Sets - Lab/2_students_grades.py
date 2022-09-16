# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N.
# On the following N lines, you will be receiving a student's name and their grade.
# For each student print all his/her grades and finally his/her average grade,
# formatted to the second decimal point in the format:
# "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.

students = {}

for none in range(int(input())):
    name_grade = tuple(input().split())
    name, grade = name_grade
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for key, value in students.items():
    avg = sum(value) / len(value)
    print(f'{key} -> {" ".join([f"{x:.2f}" for x in value])} (avg: {avg:.2f})')
