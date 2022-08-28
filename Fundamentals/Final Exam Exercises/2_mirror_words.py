# The SoftUni Spelling Bee competition is here. But it`s not like any other Spelling Bee competition out there.
# It`s different and a lot more fun! You, of course, are a participant, and you are eager to show the competition that
# you are the best, so go ahead, learn the rules and win!
# On the first line of the input, you will be given a text string.
# To win the competition, you have to find all hidden word pairs, read them,
# and mark the ones that are mirror images of each other.
# First of all, you have to extract the hidden word pairs. Hidden word pairs are:
# •	Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
# •	At least 3 characters long each (without the surrounding symbols)
# •	Made up of letters only
# If the second word, spelled backward, is the same as the first word and vice versa (casing matters!),
# they are a match, and you have to store them somewhere. Examples of mirror words:
# #Part##traP# @leveL@@Level@ #sAw##wAs#
# •	If you don`t find any valid pairs, print: "No word pairs found!"
# •	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
# •	If there are no mirror words, print: "No mirror words!"
# •	If there are mirror words print:
# "The mirror words are:
# {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"

import re

text = input()
regex = "(?P<words>(@[a-zA-Z]{3,})@@([a-zA-Z]{3,})@)|(?P<words2>(#[a-zA-Z]{3,})##([a-zA-Z]{3,})#)"
matches = re.finditer(regex, text)
words = []
results = []
for match in matches:
    words.append(match[0])
for word in words:
    i = int(len(word) / 2)
    first = word[:i]
    second = word[i:]
    if first == second[::-1]:
        pair = [f"{first[1:-1]} <=> {second[1:-1]}"]
        results += pair
if len(words) >= 1:
    print(f"{len(words)} word pairs found!")
else:
    print(f"No word pairs found!")
if len(results) >= 1:
    print("The mirror words are:")
    print(", ".join(results))
else:
    print("No mirror words!")
