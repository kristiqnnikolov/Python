liked = {}
disliked = {}
unliked_meals = 0
current_command = input()
while not current_command == 'Stop':
    command = current_command.split("-")
    like_dislike = command[0]
    guest = command[1]
    meal = command[2]
    if like_dislike == 'Like':
        if guest not in liked:
            liked[guest] = []
        if meal not in liked[guest]:
            liked[guest].append(meal)
    elif like_dislike == 'Dislike':
        if guest in liked:
            if meal in liked[guest]:
                liked[guest].remove(meal)
                unliked_meals += 1
                print(f"{guest} doesn't like the {meal}.")
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest} is not at the party.")

    current_command = input()
for guest, meal in liked.items():
    print(f"{guest}: {', '.join(meal)}")
print(f"Unliked meals: {unliked_meals}")