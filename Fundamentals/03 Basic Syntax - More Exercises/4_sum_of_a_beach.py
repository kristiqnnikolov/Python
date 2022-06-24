# Beaches are filled with sand, water, fish, and sun.
# Given a string, calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (case insensitive).


text = input()
text = text.lower()
total = text.count("sun") + text.count("fish") + text.count("sand") + text.count("water")
print(total)
