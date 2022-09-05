# Hot Potato is a game in which children form a circle and start tossing a hot potato.
# The counting starts with the first kid. Every nth toss the child who is holding the potato leaves the game.
# When a kid leaves the game, it passes the potato to the next kid. This continues until there is only one kid left.
# Create a program that simulates the game of Hot Potato.
# On the first line you will receive names of kids, separated by a single space.
# On the second line you will receive the nth toss (integer) in which a child leaves the game.
# Print every kid which is removed from the circle in the format "Removed {kid}".
# In the end, print the only kid left in the format "Last is {kid}".

from collections import deque

names = deque(input().split())
toss = int(input())

while len(names) > 1:
    names.rotate(-toss)
    print(f"Removed {names.pop()}")
print(f"Last is {names.popleft()}")

