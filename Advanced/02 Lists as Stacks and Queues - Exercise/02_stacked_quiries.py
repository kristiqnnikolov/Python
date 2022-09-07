# You have an empty stack. You will receive an integer – N. On the next N lines you will receive queries.
# Each query is one of these four types:
# •	'1 {number}' – push the number (integer) into the stack
# •	'2' – delete the number at the top of the stack
# •	'3' – print the maximum number in the stack
# •	'4' – print the minimum number in the stack
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from the top to the bottom in the following format:
# "{n}, {n1}, {n2}, ... {nn}"
lines = int(input())
my_stack = []
for x in range(lines):
    queries = input().split()
    num = queries[0]
    if num == '1':
        number = int(queries[1])
        my_stack.append(number)
    elif num == '2' and my_stack:
        my_stack.pop()
    elif num == '3' and my_stack:
        print(max(my_stack))
    elif num == '4' and my_stack:
        print(min(my_stack))

result = []
for x in range(len(my_stack)):
    result.append(my_stack.pop())
print(*result, sep=", ")
