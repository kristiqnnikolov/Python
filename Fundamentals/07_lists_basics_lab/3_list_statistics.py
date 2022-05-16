# On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"


n = int(input())
negatives = []
positives = []
count_negatives = 0
for a in range(n):
    i = int(input())
    if i >= 0:
        positives.append(i)
    else:
        negatives.append(i)
        count_negatives += i
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {count_negatives}")
