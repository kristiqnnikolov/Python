# Write a function that, depending on the first line of the input,
# reads one of the following strings: "int", "real", or "string".
# •	If the data type is an int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# •	If the data type is a string, surround the input with "$".

def text(txt, second):
    if txt == 'int':
        return int(second) * 2
    elif txt == 'real':
        return f'{float(second) * 1.5:.2f}'
    elif txt == 'string':
        return f'${second}$'


string = input()
second_string = input()
print(text(string, second_string))
