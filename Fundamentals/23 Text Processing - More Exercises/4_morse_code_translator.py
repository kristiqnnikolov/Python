# Write a program that translates messages from Morse code to English (capital letters).
# Use this page to help you (without the numbers). The words will be separated by a space (' ').
# Each word is separated by a ' | '.
# Print the found words on one line, separated by a space.

def morse_translator(txt):
    letters = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
               'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
               'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
               'Y': '-.--', 'Z': '--..'}
    result = ""
    for word in txt:
        word = word.split()
        for i in word:
            for letter, code in letters.items():
                if i == code:
                    result += letter
        result += " "
    print(result)


message = input().split(" | ")
morse_translator(message)
