# You will be given series of strings until you receive an "end" command.
# Write a program that reverses strings and prints each pair on separate line in the format "{word} = {reversed word}".

text = input()
while not text == 'end':
    reversed = text[::-1]
    print(f'{text} = {reversed}')
    # reversed = ""
    # for char in reversed(text):
    # text_reversed += ch
    # print(text + " = " + reversed)
    text = input()
