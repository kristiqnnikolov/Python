# Trifon has finally become a junior developer and has received his first task.
# It is about manipulating a list of integers. He is not quite happy about it since he hates manipulating lists.
# They will pay him a lot of money, though, and he is willing to give somebody half of it if to help him do his job.
# On the other hand, you love lists (and money), so you decide to try your luck.
# The list may be manipulated by one of the following commands:
# •	"exchange {index}" – splits the list after the given index and exchanges the places of the two resulting sub-lists.
# E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]
# -	If the index is outside the boundaries of the list, print "Invalid index"
# -	A negative index is considered invalid
# •	"max even/odd"– returns the INDEX of the max even/odd element. E.g., [1, 4, 8, 2, 3] -> "max odd" -> print: 4
# •	"min even/odd" – returns the INDEX of the min even/odd element. E.g. [1, 4, 8, 2, 3] -> "min even" -> print: 3
# -	If there are two or more equal min/max elements, return the index of the rightmost one
# -	If a min/max even/odd element cannot be found, print "No matches"
# •	"first {count} even/odd" –returns the first count even/odd elements. E.g. [1, 8, 2, 3]->"first 2 even"->print [8, 2]
# •	"last {count} even/odd" –returns the last count even/odd elements. E.g. [1, 8, 2, 3]->"last 2 odd"->print [1, 3]
# -	If the count is greater than the list length, print "Invalid count"
# -	If there are not enough elements to satisfy the count, print as many as you can.
# If there are zero even/odd elements, print an empty list "[]"
# •	"end" - stop taking input and print the final state of the list


the_list = list(map(int, input().split()))
current_command = input()

while not current_command == 'end':
    command = current_command.split()
    temp = []
    if command[0] == 'exchange':
        i = int(command[1])
        if i >= len(the_list) or i < 0:
            print('Invalid index')
        else:
            the_list = the_list[i + 1:] + the_list[:i + 1]
    elif command[0] == 'max' or command[0] == 'min':
        for i in the_list:
            if command[1] == 'even':
                if i % 2 == 0:
                    temp.append(i)
            elif command[1] == 'odd':
                if i % 2 != 0:
                    temp.append(i)
        if temp:
            if command[0] == 'max':
                temp_list = max(temp)
            elif command[0] == 'min':
                temp_list = min(temp)
            for i in range(len(the_list) - 1, -1, -1):
                if the_list[i] == temp_list:
                    print(i)
                    break
        else:
            print('No matches')
    elif command[0] == 'first':
        count = int(command[1])
        if count <= len(the_list):
            for i in the_list:
                if command[2] == 'even':
                    if i % 2 == 0:
                        temp.append(i)
                elif command[2] == 'odd':
                    if i % 2 != 0:
                        temp.append(i)
                if len(temp) == count:
                    break
            print(temp)
        else:
            print('Invalid count')
    elif command[0] == 'last':
        count = int(command[1])
        if count <= len(the_list):
            for i in reversed(the_list):
                if command[2] == 'even':
                    if i % 2 == 0:
                        temp.append(i)
                elif command[2] == 'odd':
                    if i % 2 != 0:
                        temp.append(i)
                        if len(temp) == count:
                            break
            print(temp[::-1])
        else:
            print('Invalid count')
    current_command = input()
print(the_list)
