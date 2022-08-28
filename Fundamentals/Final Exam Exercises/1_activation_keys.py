# You are about to make some good money, but first, you need to think of a way to verify who
# paid for your product and who didn't.
# You have decided to let people use the software for a free trial period and then require an activation key to
# continue using the product. Before you can cash out, the last step is to design a program that creates unique
# activation keys for each user. So, waste no more time and start typing!
# The first line of the input will be your raw activation key. It will consist of letters and numbers only.
# After that, until the "Generate" command is given, you will be receiving strings with instructions for different
# operations that need to be performed upon the raw activation key.
# There are several types of instructions, split by ">>>":
# •	"Contains>>>{substring}":
# o	If the raw activation key contains the given substring, prints: "{raw activation key} contains {substring}".
# o	Otherwise, prints: "Substring not found!"
# •	"Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
# o	Changes the substring between the given indices (the end index is exclusive)
# to upper or lower case and then prints the activation key.
# o	All given indexes will be valid.
# •	"Slice>>>{startIndex}>>>{endIndex}":
# o	Deletes the characters between the start and end indices (the end index is exclusive) and prints the activation key.
# o	Both indices will be valid.

text = input()

current_command = input()
while not current_command == 'Generate':
    command = current_command.split(">>>")
    action = command[0]
    if action == 'Contains':
        substring = command[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print(f"Substring not found!")
    elif action == 'Flip':
        direction = command[1]
        start = int(command[2])
        end = int(command[3])
        part = text[start:end]
        if direction == 'Upper':
            x = part.upper()
            text = text.replace(part, x)
        else:
            x = part.lower()
            text = text.replace(part, x)
        print(text)
    elif action == 'Slice':
        start = int(command[1])
        end = int(command[2])
        text = text[:start] + text[end:]
        print(text)
    current_command = input()
print(f"Your activation key is: {text}")
