# Yet again, you have forgotten your password. Naturally, it's not the first time this has happened.
# Actually, you got so tired of it that you decided to help yourself with an intelligent solution.
# Write a password reset program that performs a series of commands upon a predefined string.
# First, you will receive a string, and afterward, until the command "Done" is given,
# you will be receiving strings with commands split by a single space. The commands will be the following:
# •	"TakeOdd"
# o	 Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
# •	"Cut {index} {length}"
# o	Gets the substring with the given length starting from the given index from the password and
# removes its first occurrence, then prints the password on the console.
# o	The given index and the length will always be valid.
# •	"Substitute {substring} {substitute}"
# o	If the raw password contains the given substring, replaces all of its occurrences with
# the substitute text given and prints the result.
# o	If it doesn't, prints "Nothing to replace!".

text = input()

current_command = input()
while not current_command == 'Done':
    command = current_command.split()
    action = command[0]
    if action == 'TakeOdd':
        result = ""
        for i in range(len(text)):
            if not i % 2 == 0:
                result += text[i]
        text = result
        print(text)
    elif action == 'Cut':
        index = int(command[1])
        length = int(command[2])
        text = text[:index] + text[index + length:]
        print(text)
    elif action == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")
    current_command = input()
print(f"Your password is: {text}")
