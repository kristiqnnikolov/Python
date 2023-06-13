# First you will be given a sequence of integers representing males.
# Afterwards you will be given another sequence of integers representing females.
# You have to start from the first female and try to match it with the last male.
# •	If their values are equal, you have to match them and remove both of them.
# Otherwise you should remove only the female and decrease the value of the male by 2.
# •	If someone’s value is equal to or below 0, you should remove him/her from the
# records before trying to match him/her with anybody.
# •	Special case - if someone’s value divisible by 25 without remainder,
# you should remove him/her and the next person of the same gender before trying to match them with anybody.
# You need to stop matching people when you have no more females or males.
# Input
# •	On the first line of input you will receive the integers, representing the males, separated by a single space.
# •	On the second line of input you will receive the integers, representing the females, separated by a single space.
# Output
# •	On the first line of output - print the number of successful matches:
# o	"Matches: {matchesCount}"
# •	On the second line - print all males left:
# o	If there are no males: "Males left: none"
# o	If there are males: "Males left: {maleN}, … , {male3}, {male2}, {male1}"
# •	On the third line - print all females left:
# o	If there are no females: "Females left: none"
# o	If there are females: "Females left: {female1}, {female2}, {female3},…, {femaleN}"
from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] <= 0:
        females.popleft()
        continue

    if males[-1] % 25 == 0:
        males.pop()
        continue
    if females[0] % 25 == 0:
        females.popleft()
        continue

    if males[-1] == females[0]:
        males.pop()
        matches += 1
    else:
        males[-1] -= 2
    females.popleft()

print(f"Matches: {matches}")
if males:
    print(f'Males left: {", ".join(str(x) for x in males[::-1])}')
else:
    print(f'Males left: none')
if females:
    print(f'Females left: {", ".join(str(x) for x in females)}')
else:
    print(f'Females left: none')
