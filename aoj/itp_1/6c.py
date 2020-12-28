people = [[[0 for _ in range(10)]for _ in range(3)]for _ in range(4)]

n = int(input())
for i in range(n):
    lc = list(map(int, input().split()))
    b = lc[0]
    f = lc[1]
    r = lc[2]
    p = lc[3]
    people[b-1][f-1][r-1] += p

for k in range(4):
    for l in range(3):
        print('', *people[k][l])
    if not k == 3:
        print('####################')
