n, m, t = map(int, input().split())
n_max = n
last = 0
for _ in range(m):
    a, b = map(int, input().split())
    n -= a-last
    if n <= 0:
        print("No")
        exit()
    n = min(n_max, n+b-a)
    last = b
print("Yes" if n-(t-last) > 0 else "No")


# Rferenc:e https://atcoder.jp/contests/abc185/submissions/18951575
