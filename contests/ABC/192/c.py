N, K = map(int, input().split())

for i in range(K):
    if N == 0:
        break
    g2 = ''.join(sorted(str(N)))
    g1 = ''.join(reversed(g2))

    f = int(g1)-int(g2)
    N = f
print(N)
