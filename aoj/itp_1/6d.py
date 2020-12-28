n, m = map(int, input().split())

a = [[0 for _ in range(m)] for _ in range(n)]
b = []

for i in range(n):
    lc = list(map(int, input().split()))
    a[i] = lc

for j in range(m):
    b.append(int(input()))

for k in range(n):
    c = 0
    for l in range(m):
        c += a[k][l]*b[l]
    print(c)
