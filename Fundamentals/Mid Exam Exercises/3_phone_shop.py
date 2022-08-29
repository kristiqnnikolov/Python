phones = input().split(', ')
current_command = input()
while current_command != 'End':
    command = current_command.split(" - ")
    deed = command[0]
    phone = command[1]
    if deed == 'Add':
        if phone not in phones:
            phones.insert(-1, phone)
    elif deed == 'Remove':
        if phone in phones:
            phones.remove(phone)
    elif deed == 'Bonus phone':
        current = phone.split(':')
        old = current[0]
        new = current[1]
        if old in phones:
            index_old = phones.index(old)
            phones.insert(index_old + 1, new)
    elif deed == 'Last':
        if phone in phones:
            phones.remove(phone)
            phones.append(phone)
    current_command = input()
print(*phones, sep=', ')
