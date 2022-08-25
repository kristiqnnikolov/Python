# Write a program that reads a string from the console that contains:
# •	Explosions marked with '>'
# •	Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
# •	Any other characters
# Your task is to delete x characters, starting after the exploded character ('>').
# If you find another explosion mark ('>') while deleting characters,
# you should add the strength to your previous explosion. You should not delete the explosion character – '>'.
# When all characters are processed, print the final string.

def explosion(text):
    power = 0
    txt = ""
    for i in range(len(text)):
        if text[i] != ">" and power > 0:
            power -= 1
        elif text[i] == ">":
            power += int(text[i + 1])
            txt += ">"
        else:
            txt += text[i]
    print(txt)


data = input()
explosion(data)
