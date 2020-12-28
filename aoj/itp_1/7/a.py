scores = []
while True:
    score = list(map(int, input().split()))
    m = score[0]
    f = score[1]
    r = score[2]
    if m == f == r == -1:
        break
    scores.append(score)


for score in scores:
    m = score[0]
    f = score[1]
    r = score[2]
    sum = m+f

    if m == -1 or f == -1:
        print('F')
    elif 80 <= sum:
        print('A')
    elif 65 <= sum < 80:
        print('B')
    elif 50 <= sum < 65:
        print('C')
    elif 30 <= sum < 50:
        if 50 <= r:
            print('C')
        else:
            print('D')
    else:
        print('F')
