# You have plenty of free time, so you decide to write a program that conceals and reveals your received messages.
# Go ahead and type it in!
# On the first line of the input, you will receive the concealed message.
# After that, until the "Reveal" command is given, you will receive strings with instructions for different operations
# that need to be performed upon the concealed message to interpret it and reveal its actual content.
# There are several types of instructions, split by ":|:"
# •	"InsertSpace:|:{index}":
# o	Inserts a single space at the given index. The given index will always be valid.
# •	"Reverse:|:{substring}":
# o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
# o	If not, print "error".
# o	This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
# •	"ChangeAll:|:{substring}:|:{replacement}":
# o	Changes all occurrences of the given substring with the replacement text.

txt = input()
current_command = input()
while not current_command == 'Reveal':
    command = current_command.split(":|:")
    action = command[0]
    if action == 'InsertSpace':
        index = int(command[1])
        start = txt[:index]
        end = txt[index:]
        txt = start + " " + end
        print(txt)
    elif action == 'Reverse':
        subs = command[1]
        if subs in txt:
            replacer = subs[::-1]
            txt = txt.replace(subs, "", 1)
            txt += replacer
            print(txt)
        else:
            print("error")
    elif action == 'ChangeAll':
        subs = command[1]
        replacer = command[2]
        txt = txt.replace(subs, replacer)
        print(txt)
    current_command = input()

print(f"You have a new text message: {txt}")
