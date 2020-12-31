cheeseboards = []

data = []

while True:
    h, w = map(int, input().split())
    if h == w == 0:
        break

    data.append([h, w])

    cheeseboard = []

    for i in range(h):
        col = ''
        for j in range(w):
            if (i % 2 != 0 and j % 2 != 0) or (i % 2 == 0 and j % 2 == 0):
                col += '#'
            else:
                col += '.'
        cheeseboard.append(col)

    cheeseboards.append(cheeseboard)

for c in cheeseboards:
    for i in range(len(c)):
        print(c[i])
    print('')
