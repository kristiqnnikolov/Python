# If you can't fall asleep, try counting sheep!
# You will be given a positive integer, 3, for example.
# You should return a string with a murmur: "1 sheep...2 sheep...3 sheep..."
# Input will always be valid, i.e., integers greater than 0.


number = int(input())
if number > 0:
    for x in range(1, number + 1):
        print(f"{x} sheep...", end="")
