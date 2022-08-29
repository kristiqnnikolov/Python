# Create a program that calculates bonus points for each student enrolled in a course.
# On the first line, you are going to receive the number of the students.
# On the second line, you will receive the total number of lectures in the course.
# The course has an additional bonus, which you will receive on the third line.
# On the following lines, you will be receiving the count of attendances for each student.
# The bonus is calculated with the following formula:
# {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
# Find the student with the maximum bonus and print them, along with his attendances, in the following format:
# "Max Bonus: {max bonus points}."
# "The student has attended {student attendances} lectures."
# Round the bonus points at the end to the nearest larger number.

number_of_students = int(input())
lectures = int(input())
bonus = int(input())
higher_attendance = 0
current_student = 0
for student in range(1, number_of_students + 1):
    studentt = int(input())
    total_bonus = studentt / lectures * (5 + bonus)
    if total_bonus > higher_attendance:
        higher_attendance = total_bonus
        current_student = studentt
print(f"Max Bonus: {round(higher_attendance)}.")
print(f"The student has attended {current_student} lectures.")
