# Write a program, which keeps a dictionary with synonyms. The key of the dictionary will be the word.
# The value will be a list of all the synonyms of that word. You will be given a number n – the count of the words.
# After each term, you will be given a synonym, so the count of lines you should read from the console is 2 * n.
# You will be receiving a word and a synonym each on a separate line like this:
# •	{word}
# •	{synonym}
# If you get the same word twice, just add the new synonym to the list.
# Print the words in the following format:
# {word} - {synonym1, synonym2 … synonymN}

loops = int(input())
my_dict = {}
for x in range(1, loops + 1):
    key = input()
    value = input()
    if key not in my_dict:
        my_dict.get(key)
        my_dict[key] = value
    else:
        my_dict[key] += ', ' + value
for key, value in my_dict.items():
    print(f'{key} - {value}')
