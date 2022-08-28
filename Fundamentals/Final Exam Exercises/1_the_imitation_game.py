# During World War 2, you are a mathematician who has joined the cryptography team to decipher the enemy's enigma code.
# Your job is to create a program to crack the codes.
# On the first line of the input, you will receive the encrypted message.
# After that, until the "Decode" command is given,
# you will be receiving strings with instructions for different operations that need to be performed upon the concealed
# message to interpret it and reveal its true content. There are several types of instructions, split by '|'
# •	"Move {number of letters}":
# o	Moves the first n letters to the back of the string
# •	"Insert {index} {value}":
# o	Inserts the given value before the given index in the string
# •	"ChangeAll {substring} {replacement}":
# o	Changes all occurrences of the given substring with the replacement text

message = input()
text = input()
while not text == 'Decode':
    txt = text.split("|")
    action = txt[0]
    if action == 'Move':
        num = int(txt[1])
        temp = message[:num]
        cut = message[num:]
        message = cut + temp
    elif action == 'Insert':
        i = int(txt[1])
        letter = txt[2]
        first = message[:i]
        second = message[i:]
        message = first + letter + second
    elif action == 'ChangeAll':
        letter = txt[1]
        replacer = txt[2]
        if letter in message:
            message = message.replace(letter, replacer)
    text = input()

print(f"The decrypted message is: {message}")
