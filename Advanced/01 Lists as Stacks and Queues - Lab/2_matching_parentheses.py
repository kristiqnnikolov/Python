# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# Print the result back on the console.

text = input()

indexes = []

for i in range(len(text)):
    if text[i] == "(":
        indexes.append(i)
    elif text[i] == ")":
        start = indexes.pop()
        result = text[start:i+1]
        print(result)
