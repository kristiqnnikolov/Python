# Valentine's Day is coming, and Cupid has minimal time to spread some love across the neighborhood.
# Help him with his mission!
# You will receive a string with even integers, separated by a "@" - this is our neighborhood.
# After that, a series of Jump commands will follow until you receive "Love!".
# Every house in the neighborhood needs a certain number of hearts delivered by Cupid so
# it can celebrate Valentine's Day. The integers in the neighborhood indicate those needed hearts.
# Cupid starts at the position of the first house (index 0) and must jump by a given length.
# The jump commands will be in this format: "Jump {length}".
# Every time he jumps from one house to another, the needed hearts for the visited house are decreased by 2:
# •	If the needed hearts for a certain house become equal to 0,
# print on the console "Place {house_index} has Valentine's day."
# •	If Cupid jumps to a house where the needed hearts are already 0,
# print on the console "Place {house_index} already had Valentine's day."
# •	Keep in mind that Cupid can have a larger jump length than the size of the neighborhood, and
# if he does jump outside of it, he should start from the first house again (index 0)

def after_math(input, last_position):
    result = [el for el in input if el == 0]
    print(f"Cupid's last position was {last_position}.")

    if len(result) != len(input):
        difference = len(input) - len(result)
        print(f"Cupid has failed {difference} places.")
    else:
        print("Mission was successful.")


def heart_delivery(numbers):
    current_index = 0
    last_position = 0
    while True:
        command = input().split(' ')
        if command[0] == 'Love!':
            break
        index = int(command[1]) + current_index
        if index >= len(numbers):
            index = 0
        if -1 < index < len(numbers):
            if numbers[index] > 0:
                numbers[index] -= 2
                if numbers[index] == 0:
                    print(f"Place {index} has Valentine's day.")
            else:
                print(f"Place {index} already had Valentine's day.")
        current_index = index
        last_position = index
    after_math(numbers, last_position)


strings = list(map(int, input().split('@')))
heart_delivery(strings)
