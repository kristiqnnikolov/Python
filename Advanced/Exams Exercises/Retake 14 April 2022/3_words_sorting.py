# Write a function words_sorting which receives a different number of words.
# Create a dictionary, which will have as keys the words that the function received.
# For each key, create a value that is the sum of all ASCII values of that key.
# Then, sort the dictionary:
# •	By values in descending order, if the sum of all values of the dictionary is odd
# •	By keys in ascending order, if the sum of all values of the dictionary is even
# Note: Submit only the function in the judge system
# Input
# •	There will be no input, just any number of words passed to your function
# Output
# •	The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
def words_sorting(*args):
    words = {}
    result = ""
    all_sum = 0
    for word in args:
        current_sum = 0
        for x in word:
            current_sum += ord(x)
        all_sum += current_sum
        words[word] = current_sum
    if all_sum % 2 == 0:
        for word, current_sum in sorted(words.items(), key=lambda kvpt: kvpt[0]):
            result += f'{word} - {current_sum}\n'
    else:
        for word, current_sum in sorted(words.items(), key=lambda kvpt: -kvpt[1]):
            result += f'{word} - {current_sum}\n'
    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))

print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
