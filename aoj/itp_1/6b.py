cards = [[0 for j in range(13)] for i in range(4)]
times = int(input())
for _ in range(times):
    lc = list(map(str, input().split()))
    s = lc[0]
    n = int(lc[1])
    if s == 'S':
        cards[0][n-1] = (n)
    elif s == 'H':
        cards[1][n-1] = (n)
    elif s == 'C':
        cards[2][n-1] = (n)
    elif s == 'D':
        cards[3][n-1] = (n)
    else:
        exit()
        print("ERROR")

for i in range(4):
    for j in range(13):
        if i == 0 and cards[i][j] == 0:
            print('S {0}'.format(j+1))
        elif i == 1 and cards[i][j] == 0:
            print('H {0}'.format(j+1))
        elif i == 2 and cards[i][j] == 0:
            print('C {0}'.format(j+1))
        elif i == 3 and cards[i][j] == 0:
            print('D {0}'.format(j+1))
