# You are a facility manager at a large business center.
# One of your responsibilities is to check if each conference room in the center has enough chairs for the visitors.
# On the first line, you will be given an integer n representing the number of rooms in the business center.
# On the following n lines for each room, you will receive information about
# the chairs in the room and the number of visitors. Each chair will be presented with the char "X".
# Next, there will be a single space and the number of visitors at the end.
# For example: "XXXXX 4" (5 chairs and 4 visitors).
# Keep track of the free chairs:
# •	If there are not enough chairs in a specific room, print the following message:
# "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
# •	Otherwise, print: "Game On, {total_free_chairs} free chairs left".

def office(numbers_of_rooms):
    chairs_left = 0
    is_not_full = True
    for room_number in range(1, numbers_of_rooms + 1):
        nums = input().split(' ')
        chairs = nums[0]
        visitors = int(nums[1])
        difference = abs(len(chairs) - visitors)
        if len(chairs) < visitors:
            is_not_full = False
            print(f'{difference} more chairs needed in room {room_number}')
        elif len(chairs) > visitors:
            chairs_left += difference

    if is_not_full:
        print(f'Game On, {chairs_left} free chairs left')


rooms = int(input())
office(rooms)
