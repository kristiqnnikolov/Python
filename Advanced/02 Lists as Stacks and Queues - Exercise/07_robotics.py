# Somewhere in the future, there is a robotics factory. The current project is assembly line robots.
# Each robot has a processing time – it is the time in seconds the robot needs to process a product.
# When a robot is free it should take a product for processing and log his name, product and processing start time.
# Each robot processes a product coming from the assembly line. A product is coming from the line each second
# (so the first product should appear at [start time + 1 second]).
# If a product passes the line and there is not a free robot to take it,
# it should be queued at the end of the line again.
# The robots are standing on the line in the order of their appearance.
# Input
# •	On the first line, you will receive the names of the robots and their processing times in the format
# "robotName-processTime;robotName-processTime;robotName-processTime..."
# •	On the second line, you will get the starting time in format "hh:mm:ss"
# •	Next, until the "End" command, you will get a product on each line.
# Output
# •	Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"
from collections import deque


def clock_time(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots_data = input().split(";")
clock = [int(x) for x in input().split(":")]

total_seconds = clock[0] * 3600 + clock[1] * 60 + clock[2]
items = deque()
robots = {}
busy_robots = {}

for data in robots_data:
    info = data.split('-')
    name = info[0]
    time = info[1]
    robots[name] = int(time)
    busy_robots[name] = -1

item = input()
while not item == 'End':
    items.append(item)
    item = input()

while items:
    total_seconds += 1
    item = items.popleft()
    for robot, working_time in busy_robots.items():
        if total_seconds >= working_time:
            busy_robots[robot] = total_seconds + robots[robot]
            time = clock_time(total_seconds)
            print(f'{robot} - {item} [{time}]')
            break
    else:
        items.append(item)
