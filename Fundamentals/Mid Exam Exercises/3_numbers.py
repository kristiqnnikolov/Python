numbers = input()
integers = [int(x) for x in numbers.split()]
integers.sort(reverse=True)
average = sum(integers) / len(integers)
counter = 0
result = ''
for numbers in range(len(integers)):
    if integers[numbers] > average:
        result += str(integers[numbers]) + ' '
        counter += 1
        if counter == 5:
            break
if result == '':
    result += 'No'
print(result)
