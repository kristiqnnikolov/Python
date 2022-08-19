# The lottery is exciting. However, checking a million tickets for winnings only by hand is not.
# So, you are given the task of creating a program that automatically checks if a ticket is a winner.
# You are given a collection of tickets separated by commas and spaces (one or many).
# You need to check each ticket to see if it has a winning combination of symbols:
# •	A valid ticket has exactly 20 characters.
# •	A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^'
# uninterruptedly repeated at least 6 times in both halves of the tickets.
# •	In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides
# An example of a valid winning ticket:
# "Cash$$$$$$Ca$$$$$$sh"
# An example of a Jackpot winning valid ticket:
# "$$$$$$$$$$$$$$$$$$$$"

def winning(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    left = ticket[:10]
    right = ticket[10:]
    symbols = ['@', '#', '$', '^']
    for symbol in symbols:
        for row in range(10, 5, -1):
            streak = symbol * row
            if streak in left and streak in right:
                if row == 10:
                    return f'ticket "{ticket}" - {len(streak)}{symbol} Jackpot!'
                else:
                    return f'ticket "{ticket}" - {len(streak)}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [s.strip() for s in input().split(', ')]
result = []
for ticket in tickets:
    result.append(winning(ticket))
for state in result:
    print(state)
