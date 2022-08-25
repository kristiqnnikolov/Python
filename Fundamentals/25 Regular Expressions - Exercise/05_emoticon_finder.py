# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.

def emoticon_finder(data):
    for char in range(0, len(data)):
        if data[char] == ":":
            print(data[char] + data[char + 1])


text = input()
emoticon_finder(text)
