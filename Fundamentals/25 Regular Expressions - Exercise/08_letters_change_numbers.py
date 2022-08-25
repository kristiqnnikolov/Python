# John invented a game with numbers and letters from the English alphabet. The game was simple.
# You receive a string consisting of a number between two letters.
# For the given string, you should perform different mathematical operations to achieve a result:
# •	First, if the letter in front of the number is:
# o	Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
# o	Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
# •	Next, if the letter after the number is:
# o	Uppercase: subtract its position from the resulting number (starting from 1)
# o	Lowercase: add its position to the resulting number (starting from 1)
# The game was too easy for John. He decided to complicate it by doing the same calculations to
# multiple strings keeping track of only the total sum of all results.
# Once he started to solve this with more strings and bigger numbers, it became quite hard to do it only in his mind.
# He kindly asks you to write a program that performs the operations
# described above and sums the final results of each string.

def letters(data):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    total = 0
    for word in data:
        if word[0].isalpha:
            first = word[0]
        if word[-1].isalpha:
            second = word[-1]
        number = word[1:-1]
        result = 0
        if first.isupper():
            for i in range(len(alphabet)):
                if first == alphabet[i]:
                    num = int(i) + 1
                    if result == 0:
                        result += int(number) / num
                    else:
                        result /= num
        if first.islower():
            for i in range(len(lower_alphabet)):
                if first == lower_alphabet[i]:
                    num = int(i) + 1
                    if result == 0:
                        result += int(number) * num
                    else:
                        result *= num
        if second.isupper():
            for i in range(len(alphabet)):
                if second == alphabet[i]:
                    num = int(i) + 1
                    if result == 0:
                        result += int(number) - num
                    else:
                        result -= num
        if second.islower():
            for i in range(len(lower_alphabet)):
                if second == lower_alphabet[i]:
                    num = int(i) + 1
                    if result == 0:
                        result += int(number) + num
                    else:
                        result += num
        total += result
    print(f'{total:.2f}')


text = input().split()
letters(text)
