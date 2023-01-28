# Write a program which finds the longest intersection. You will be given a number N.
# On each of the next N lines you will be given two ranges in the format:
# "{first_start},{first_end}-{second_start},{second_end}". You should find the intersection of these two ranges.
# The start and end numbers in the ranges are inclusive.
# Finally, you should find the longest intersection of all N intersections,
# print the numbers that are included and its length in the format:
# "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
# Note: in each range, there will always be intersection. If there are two equal intersections, print the first one.


longest = set()

for none in range(int(input())):
    line = input().split('-')
    first = line[0].split(',')
    second = line[1].split(',')
    one, two = int(first[0]), int(first[1])
    three, four = int(second[0]), int(second[1])

    first_set = set()
    second_set = set()

    for x in range(one, two + 1, 1):
        first_set.add(x)
    for i in range(three, four + 1, 1):
        second_set.add(i)

    first_set = first_set.intersection(second_set)

    if len(first_set) > len(longest):
        longest = [x for x in first_set]

print(f'Longest intersection is {longest} with length {len(longest)}')