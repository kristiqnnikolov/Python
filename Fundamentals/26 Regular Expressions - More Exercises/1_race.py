# Write a program that processes information about a race.
# On the first line you will be given list of participants separated by ", ".
# On the next few lines until you receive a line "end of race" you will be given some info which will be some
# alphanumeric characters. In between them you could have some extra characters which you should ignore.
# For example: "G!32e%o7r#32g$235@!2e".
# The letters are the name of the person and the sum of the digits is the distance he ran.
# So here we have George who ran 29 km.
# Store the information about the person only if the list of racers contains the name of the person.
# If you receive the same person more than once just add the distance to his old distance.
# At the end print the top 3 racers ordered by distance in descending in the format:
# "1st place: {first racer}
# 2nd place: {second racer}
# 3rd place: {third racer}"

import re

names = input().split(', ')
race = []
for name in names:
    race.append([0, name])
command = input()

all_letters = r"[a-zA-Z]"
all_numbers = r"\d"

while not command == 'end of race':
    person = ""
    km = 0
    letters = re.findall(all_letters, command)
    numbers = re.findall(all_numbers, command)
    for x in letters:
        person += x
    for a in numbers:
        km += int(a)
    for i in race:
        if i[1] == person:
            i[0] += km

    command = input()

race = sorted(race)
first = race[-1]
second = race[-2]
third = race[-3]
print(f'1st place: {first[1]}')
print(f'2nd place: {second[1]}')
print(f'3rd place: {third[1]}')
