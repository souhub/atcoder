decks = []

while True:
    deck = input()

    if deck == '-':
        break

    m = int(input())

    for i in range(m):
        h = int(input())
        deck = deck[h:]+deck[:h]
    decks.append(deck)

for sorted_deck in decks:
    print(sorted_deck)
