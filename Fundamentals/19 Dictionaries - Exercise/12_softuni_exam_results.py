# Judge statistics on the last Programing Fundamentals exam were not working correctly,
# so you have the task of taking all the submissions and analyzing them properly.
# You should collect all the submissions and print the final results and statistics
# about each language in which the participants submitted their solutions.
# You will be receiving lines in the following format:
# "{username}-{language}-{points}" until you receive "exam finished".
# You should store each username and their submissions and points.
# If a student has two or more submissions for the same language, save only his maximum points.
# You can receive a command to ban a user for cheating in the following format: "{username}-banned".
# In that case, you should remove the user from the contest but
# preserve his submissions in the total count of submissions for each language.
# After receiving "exam finished", print each of the participants in the following format:
# "Results:
# {username1} | {points}
# {username2} | {points}
# …
# {usernameN} | {points}"
# After that, print each language used in the exam in the following format:
# "Submissions:
# {language1} - {submissions_count}
# {language2} - {submissions_count}
# …
# {language3} - {submissions_count}"

command = input()
students = {}
submissions = {}

while not command == 'exam finished':
    current = command.split("-")
    name = current[0]
    module = current[1]
    if not module == 'banned':
        if module not in submissions:
            submissions[module] = 0
        submissions[module] += 1
        points = int(current[2])
        students[name] = max(students.get(name, 0), points)
    else:
        students.pop(name)

    command = input()
print(f'Results:')
for key, value in students.items():
    print(f'{key} | {value}')
print(f'Submissions:')
for key, value in submissions.items():
    print(f'{key} - {value}')
