# You will have to find all possible color combinations that can be used.
# Write a program that finds colors in a string. You will be given a string on a single line containing substrings
# (separated by a single space) from which you will be able to form the following colors:
# Main colors: "red", "yellow", "blue"
# Secondary colors: "orange", "purple", "green"
# To form a color, you should concatenate the first and the last substrings and check if you can get any of the above
# colors' names. If there is only one substring left, you should use it to do the same check.
# You can only keep a secondary color if the two main colors needed for
# its creation could be formed from the given substrings:
# •	orange = red + yellow
# •	purple = red + blue
# •	green = yellow + blue
# Note: You could find some of the main colors needed to keep a secondary color after it is found.
# When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and
# You will have to find all possible color combinations that can be used.
# Write a program that finds colors in a string. You will be given a string on a single line containing substrings
# (separated by a single space) from which you will be able to form the following colors:
# Main colors: "red", "yellow", "blue"
# Secondary colors: "orange", "purple", "green"
# To form a color, you should concatenate the first and the last substrings and check if you can get any of the
# above colors' names. If there is only one substring left, you should use it to do the same check.
# You can only keep a secondary color if the two main colors needed
# for its creation could be formed from the given substrings:
# •	orange = red + yellow
# •	purple = red + blue
# •	green = yellow + blue
# Note: You could find some of the main colors needed to keep a secondary color after it is found.
# When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and
# return them in the middle of the original string. If the string contains an odd number of substrings,
# you should put the substrings one position ahead.
# For example, if you are given the string "re yellow bye" you could not form a color with the substring "re" and "bye",
# so you should remove the last character and return them in the middle of the string: "r by yellow".
# In the end, print out the list with colors in the order in which they are found.
# Input
# •	Single line string
# Output
# •	The list with the collected colors
from collections import deque

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

words = deque(input().split())
colors = []

while words:
    first = words.popleft()
    second = words.pop() if words else ''

    result = first + second
    if result in main_colors or result in secondary_colors:
        colors.append(result)
        continue

    result = second + first
    if result in main_colors or result in secondary_colors:
        colors.append(result)
        continue

    first = first[:-1]
    second = second[:-1]
    if first:
        words.insert(len(words) // 2, first)
    if second:
        words.insert(len(words) // 2, second)

all_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

result = []

for color in colors:
    if color in main_colors:
        result.append(color)
    elif color in secondary_colors:
        is_valid = True
        for needed_color in all_colors[color]:
            if needed_color not in colors:
                is_valid = False
                break
        if is_valid:
            result.append(color)

print(result)
