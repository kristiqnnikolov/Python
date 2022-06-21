# You will be given two strings. Transform the first string into the second one, letter by letter.
# Print only the unique strings.
# Note: the strings will have the same lengths.


first = input()
second = input()

for i in range(len(first)):
    if first[i] != second[i]:
        replacement = second[i]
        word = first[0:i] + replacement + first[i + 1:]
        first = word
        print(first)
