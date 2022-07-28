# On the first line, you will receive words separated by a single space.
# On the second line, you will receive a palindrome.
# First, you should print a list containing all the found palindromes in the sequence.
# Then, you should print the number of occurrences of the given palindrome in the format:
# "Found palindrome {number} times".

def palindrome(text):
    palindrome_list = [word for word in text if word == word[::-1]]
    return palindrome_list


words = input().split()
searched_palindrome = input()
print(palindrome(words))
print(f"Found palindrome {words.count(searched_palindrome)} times")
