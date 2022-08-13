# You know the judge system, right?! Your job is to create a program similar to the Judge system.
# You will receive several input lines in one of the following formats:
# "{username} -> {contest} -> {points}"
# The "contest" and "username" are strings, the given "points" will be an integer number.
# You need to keep track of every contest and points of each user:
# •	If the user has already participated in the contest, update their points only if
# the new ones are more than the older ones.
# •	Otherwise, just save the data - contest, username, and points.
# Also, you need to keep individual statistics for each user - the total points of all contests
# (including even points from the same contents).
# You should end your program when you receive the command "no more time".
# At that point you should print each contest in order of input, for each contest print the
# participants ordered by points in descending order, then ordered by name in ascending order.
# After that, you should print individual statistics for every participant ordered by total points in descending order,
# and then by alphabetical order.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	Username and contest name always will be one word.
# •	Points will be an integer will be an integer in range [0, 1000].
# •	There will be no invalid input lines.
# •	If all sorting criteria fail, the order should be by order of input.
# •	The input ends when you receive the command "no more time".
# Output
# •	The output format for the contests is:
# "{constest_name}: {number_participants} participants
# 1. {username1} <::> {points}
# 2. {username2} <::> {points}
# …
# {N}. {usernameN} <::> {points}"
# •	After you print all contests, print the individual statistics for every participant.
# •	The output format is:
# "Individual standings:
# 1.	{username1} -> {total_points}
# 2.	{username} -> {total_points}
# …
# {N}. {username} -> {total_points}"
contestants = {}
name_points = {}

command = input()
while not command == 'no more time':
    data = command.split(' -> ')
    name = data[0]
    course = data[1]
    points = int(data[2])
    if course not in contestants:
        contestants[course] = {}
    if name not in contestants[course]:
        contestants[course][name] = points
    else:
        if contestants[course][name] < points:
            contestants[course][name] = points
    command = input()

for course, stats in contestants.items():
    for name, points in stats.items():
        if name not in name_points:
            name_points[name] = points
        else:
            name_points[name] += points

for course, stats in contestants.items():
    number = 1
    print(f"{course}: {len(stats)} participants")
    for name, points in sorted(stats.items(), key=lambda x: (-x[1], x[0])):
        print(f"{number}. {name} <::> {points}")
        number += 1

number = 1
print("Individual standings:")
for name, points in sorted(name_points.items(), key=lambda x: (-x[1], x[0])):
    print(f"{number}. {name} -> {points}")
    number += 1
