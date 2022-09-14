# You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced.
# A sequence of parentheses is balanced if every opening parenthesis has a corresponding
# closing parenthesis that occurs after the former. There will be no interval symbols between the parentheses.
# You will be given three types of parentheses: (), {}, and [].
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.
# Input
# •	On a single line you will receive a sequence of parentheses.
# Output
# •	For each test case, print on a new line "YES" if the parentheses are balanced.
# Otherwise, print "NO". Do not print the quotes.
brackets = input()
yes = True
first_half = []

all_brackets = {'(': ')', '[': ']', '{': '}'}
for bracket in brackets:
    if bracket not in '([{':
        if not first_half:
            yes = False
            break
        first = first_half.pop()
        if not all_brackets[first] == bracket:
            yes = False
            break
    else:
        first_half.append(bracket)

if yes:
    print("YES")
else:
    print("NO")
