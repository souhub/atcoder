n = int(input())

a = list(map(int, input().split()))

for i in range(len(a)//2):
    a[i], a[len(a)-1-i] = a[len(a)-1-i], a[i]

print(*a)
