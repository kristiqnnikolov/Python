# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family.
# First, you are going to receive the gifts you plan on buying on a single line, separated by space,
# in the following format:
# "{gift1} {gift2} {gift3}… {gift n}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# •	"OutOfStock {gift}"
# o	Find the gifts with this name in your collection, if any, and change their values to "None".
# •	"Required {gift} {index}"
# o	If the index is valid, replace the gift on the given index with the given gift.
# •	"JustInCase {gift}"
# o	Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None",
# separated by a single space in the following format: "{gift1} {gift2} {gift3} … {gift n}"


gifts = input().split()
command = input()
while not command == "No Money":
    current_command = command.split()
    current_gift = current_command[1]
    if current_command[0] == 'OutOfStock':
        for index in range(len(gifts)):
            if gifts[index] == current_gift:
                gifts[index] = "None"
    elif current_command[0] == 'Required':
        index = int(current_command[2])
        if 0 <= index < len(gifts):
            gifts[index] = current_gift
    elif current_command[0] == 'JustInCase':
        gifts[-1] = current_gift
    command = input()

for gift in gifts:
    if gift != "None":
        print(gift, end=' ')
