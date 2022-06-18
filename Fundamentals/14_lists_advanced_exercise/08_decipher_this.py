# You are given a secret message you should decipher. To do that, you need to know that in each word:
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)

string = input().split()
result = []
for x in string:
    numbers = []
    new_string = []
    word = []
    for index in x:
        if index in "0, 1, 2, 3, 4, 5, 6, 7, 8 ,9, 0":
            numbers.append(index)
        else:
            new_string.append(index)
    new_string[0], new_string[-1] = new_string[-1], new_string[0]
    new_string = ("".join(new_string))
    numbers = ("".join(numbers))
    word.append(chr(int(numbers)))
    word.append(new_string)
    word = ("".join(word))
    result.append(word)
print(" ".join(result))
