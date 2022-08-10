# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"

command = input()
company_users = {}
while not command == 'End':
    current_command = command.split(" -> ")
    company = current_command[0]
    id = current_command[1]
    if company not in company_users:
        company_users[company] = []
    if id not in company_users[company]:
        company_users[company].append(id)
    command = input()
for key, value in company_users.items():
    print(f'{key}')
    value = [f'-- {x}' for x in value]
    print(*value, sep="\n")
