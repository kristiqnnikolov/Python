# Santa Claus is always watching and seeing if children are good or bad. Only the nice children get Christmas presents,
# so Santa Claus is preparing his list this year to check which child has been good or bad.
# Write a function called naughty_or_nice_list which will receive
# •	A list representing Santa Claus' "Naughty or Nice" list full of kids' names
# •	A different number of arguments (strings) and/or keywords representing commands
# The function should sort the kids in the given Santa Claus list into 3 lists: "Nice", "Naughty", and "Not found".
# The list holds a different number of kids - tuples containing two elements:
# a counting number (integer) at the first position and a name (string) at the second position.
# For example: [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")].
# Next, the function could receive arguments and/or keywords.
# Each argument is a command. The commands could be the following:
# •	"{counting_number}-Naughty" - if there is only one tuple in the given list with the same number,
# MOVE the kid to a list with NAUGHTY kids and remove it from the Santa list. Otherwise, ignore the command.
# •	"{counting_number}-Nice" - if there is only one tuple in the given list with the same number,
# MOVE the kid to a list with NICE kids and remove it from the Santa list. Otherwise, ignore the command.
# Each keyword holds a key with a name (string), and each value will be a string ("Naughty" or "Nice"):
# •	If there is only one tuple with the same name, MOVE the kid to a list with NAUGHTY or to the list with NICE kids
# depending on the value in the keyword. Then, remove it from the Santa list.
# •	Otherwise, ignore the command.
# All remaining tuples in the given Santa's list are not found kids, and they should be MOVED to the "Not found" list.
# In the end, return the final lists, each on a new line as described below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input. Just parameters passed to your function.
# Output
# •	The function should return strings with the names on each list on separate lines,
# if there are any, otherwise skip the line:
# o	"Nice: {name1}, {name2} … {nameN}"
# o	"Naughty: {name1}, {name2} … {nameN}"
# o	"Not found: {name1}, {name2} … {nameN}"
def naughty_or_nice_list(kids, *args, **kwargs):
    santa_list = {"Nice": [], "Naughty": [], "Not found": []}

    for command in args:
        numbers = [int(x[0]) for x in kids]
        num, good_or_bad = command.split("-")
        num = int(num)
        if numbers.count(num) > 1:
            continue
        for pair in kids:
            if num == pair[0]:
                santa_list[good_or_bad].append(pair[1])
                kids.remove(pair)

    for name, bad_or_good in kwargs.items():
        names = [x[1] for x in kids]
        if names.count(name) > 1:
            continue
        for pair in kids:
            if name == pair[1]:
                santa_list[bad_or_good].append(pair[1])
                kids.remove(pair)
    result = ""
    if santa_list["Nice"]:
        result += f"Nice: {', '.join([x for x in santa_list['Nice']])}\n"
    if santa_list["Naughty"]:
        result += f"Naughty: {', '.join([x for x in santa_list['Naughty']])}\n"
    if kids:
        result += f"Not found: {', '.join([x[1] for x in kids])}"
    return result.strip()


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
