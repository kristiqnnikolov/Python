# SoftUni just got a new fancy parking lot.
# It even has online parking validation, except the online service doesn't work.
# It can only receive users' data, but it doesn't know what to do with it.
# Good thing you're on the dev team and know how to fix it, right?
# Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
# The program receives 2 types of commands:
# •	"register {username} {license_plate_number}":
# -	The system only supports one car per user at the moment, so if a user tries to register another license plate
# using the same username, the system should print:
# "ERROR: already registered with plate number {license_plate_number}"
# -	If the check above passes successfully, the user should be registered, so the system should print:
#  "{username} registered {license_plate_number} successfully"
# •	"unregister {username}":
# -	If the user is not present in the database, the system should print:
# "ERROR: user {username} not found"
# -	If the check above passes successfully, the system should print:
# "{username} unregistered successfully"
# After you execute all of the commands,
# print all the currently registered users and their license plates in the format:
# •	"{username} => {license_plate_number}"

people = int(input())
parking = {}
for a in range(1, people + 1):
    command = input().split()
    to = command[0]
    name = command[1]
    if to == 'unregister':
        if name in parking:
            print(f"{name} unregistered successfully")
            name = parking.pop(name)
            continue
        else:
            print(f"ERROR: user {name} not found")
            continue
    license_number = command[2]
    if to == 'register':
        if name not in parking:
            parking[name] = license_number
            print(f"{name} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[name]}")
for key, value in parking.items():
    print(f'{key} => {value}')
