# Create a program that receives two strings on a single line separated by a single space.
# Then, it prints the sum of their multiplied character codes as follows:
# multiply str1[0] with str2[0] and add the result to the total sum, then continue with the next two characters.
# If one of the strings is longer than the other,
# add the remaining character codes to the total sum without multiplication.

def multiplier(data):
    longest = max(data, key=len)
    data.remove(longest)
    shortest = data[0]
    total = 0
    for i in range(len(longest)):
        if i < len(shortest):
            total += ord(longest[i]) * ord(shortest[i])
        else:
            total += ord(longest[i])
    print(total)


text = input().split()
multiplier(text)
