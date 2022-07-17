# Write a program that receives a single string (integers separated by a comma and space ", "),
# finds all the zeros, and moves them to the back without messing up the other elements.
# the resulting integer list.


string = input().split(",")
new_list = []

for index in string:
    if int(index) != 0:
        new_list.append(index)
for index in string:
    if int(index) == 0:
        new_list.append(index)
integer_map = map(int, new_list)
integer_list = list(integer_map)
print(integer_list)
