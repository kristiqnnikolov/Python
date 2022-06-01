# Write a function that receives two characters and returns a single string with all the characters in between them
# (according to the ASCII code), separated by a single space. Print the result on the console.

def chars_range(ch1, ch2):
    result = []
    for a in range(ord(char_one) + 1, ord(char_two)):
        result.append(chr(a))
        return


char_one = input()
char_two = input()
print(chars_range(char_one, char_two))
