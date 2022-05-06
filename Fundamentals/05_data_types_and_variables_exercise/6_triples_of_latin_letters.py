# Write a program to read an integer N and print all triples of the first N small Latin letters,
# ordered alphabetically:

n = int(input())
for a in range(0, n):
    for b in range(0, n):
        for c in range(0, n):
            print(f"{chr(97 + a)}{chr(97 + b)}{chr(97 + c)}")
