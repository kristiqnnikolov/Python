# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved,
# such that the original bottom card is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six']
# once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space)
# and on the second line receives a count of faro shuffles that should be made.
# Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.


deck = input().split(" ")
shuffles = int(input())
left_deck = []
right_deck = []
for shuffle in range(1, shuffles + 1):
    current_deck = []
    half = int(len(deck) / 2)
    left_half = deck[:half]
    right_half = deck[half::]
    for card in range(len(left_half)):
        current_deck.append(left_half[card])
        current_deck.append(right_half[card])
    deck = current_deck
print(deck)
