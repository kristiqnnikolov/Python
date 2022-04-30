# You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example, 2018.
# Write a program that receives an integer number and finds the next happy year.

year = int(input())
year += 1
while True:
    year_as_string = str(year)
    if len(year_as_string) == len(set(year_as_string)):
        break
    year += 1
print(year_as_string)
