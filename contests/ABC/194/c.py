n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    m = i-1
    total = 0
    for j in range(0, m+1):
        total += (a[i]-a[j])**2
    ans += total
print(ans)
# I coudn't solve it
