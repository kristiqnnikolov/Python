# Write a program that finds a place for the tourist on a lift.
# Every wagon should have a maximum of 4 people on it.
# If a wagon is full, you should direct the people to the next one with space available.

people = int(input())
wagons = [int(x) for x in input().split(' ')]

free_slots = len(wagons) * 4 - sum(wagons)
if people < free_slots:
    for i in range(len(wagons)):
        while people > 0:
            if wagons[i] < 4:
                wagons[i] += 1
                people -= 1
            else:
                break
    print("The lift has empty spots!")
    print(' '.join(str(i) for i in wagons))
elif people > free_slots:
    print(f"There isn't enough space! {people - free_slots} people in a queue!")
    print(' '.join([str(4)] * len(wagons)))
else:
    print(' '.join([str(4)] * len(wagons)))
