hanako_points = 0
taro_points = 0

n = int(input())

for i in range(n):
    cards = (list(map(str, input().split())))
    taro_card = cards[0]
    hanako_card = cards[1]
    sorted_cards = sorted(cards)
    if taro_card == hanako_card:
        hanako_points += 1
        taro_points += 1
    elif sorted_cards[0] == hanako_card:
        hanako_points += 3
    elif sorted_cards[0] == taro_card:
        taro_points += 3
    else:
        print('ERROR')

print(hanako_points, taro_points)
