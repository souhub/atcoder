n = int(input())
a = list(map(int, input().split()))


ans = 0
for l in range(len(a)):
    x = a[l]
    for r in range(l, len(a)):
        x = min(x, a[r])
        ans = max(ans, x*(r-l+1))
print(ans)
