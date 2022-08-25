# Write a program that reads the path to a file and subtracts the file name and its extension.

def extract(data):
    for word in data:
        if "." in word:
            x = word.split(".")
            print(f'File name: {x[0]}')
            print(f'File extension: {x[1]}')


text = input().split('\\')
extract(text)
