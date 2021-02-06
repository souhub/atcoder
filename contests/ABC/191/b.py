n, x = map(int, input().split())
a = list(map(int, input().split()))
for i in range(len(a)-1, -1, -1):
    if a[i] == x:
        a.pop(i)

print(*a)
