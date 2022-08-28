# You are a pianist, and you like to keep a list of your favorite piano pieces.
# Create a program to help you organize it and add, change, remove pieces from it!
# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have.
# On the next n lines, the pieces themselves will follow with their composer and key,
# separated by "|" in the following format: "{piece}|{composer}|{key}".
# Then, you will be receiving different commands, each on a new line,
# separated by "|", until the "Stop" command is given:
# •	"Add|{piece}|{composer}|{key}":
# o	You need to add the given piece with the information about it to the other pieces and print:
# "{piece} by {composer} in {key} added to the collection!"
# o	If the piece is already in the collection, print:
# "{piece} is already in the collection!"
# •	"Remove|{piece}":
# o	If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# •	"ChangeKey|{piece}|{new key}":
# o	If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"

number = int(input())
collection = {}
for x in range(number):
    my_list = input().split("|")
    piece = my_list[0]
    composer = my_list[1]
    key = my_list[2]
    collection[piece] = {"composer": composer, "key": key}
current_command = input()
while not current_command == 'Stop':
    command = current_command.split("|")
    if command[0] == 'Add':
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece not in collection:
            collection[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command[0] == 'Remove':
        piece = command[1]
        if piece in collection:
            del collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == 'ChangeKey':
        piece = command[1]
        new_key = command[2]
        if piece in collection:
            collection[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    current_command = input()
for key, value in collection.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")
