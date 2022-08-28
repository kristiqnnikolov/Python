text = input()

current_command = input()
while not current_command == 'End':
    command = current_command.split()
    action = command[0]
    if action == 'Translate':
        char = command[1]
        replace = command[2]
        for i in range(len(text)):
            if char == text[i]:
                text = text.replace(char, replace)
        print(text)
    elif action == 'Includes':
        subs = command[1]
        if subs in text:
            print("True")
        else:
            print("False")
    elif action == 'Start':
        is_valid = True
        subs = command[1]
        sub = ""
        for i in text:
            sub += i
            if sub == subs:
                print("True")
                is_valid = False
                break
        if is_valid:
            print("False")
    elif action == 'Lowercase':
        new = ""
        for i in text:
            new += i.lower()
        text = new
        print(text)
    elif action == 'FindIndex':
        index = command[1]
        for z in range(len(text) - 1, -1, -1):
            if text[z] == index:
                print(z)
                break
    elif action == 'Remove':
        start = int(command[1])
        count = int(command[2])
        remove = text[start:start + count]
        text = text.replace(remove, "")
        print(text)

    current_command = input()
