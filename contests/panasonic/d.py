n = int(input())

a = list(map(int, input().split()))

total = 0

for i in range(len(a)-1):
    for j in range(i, len(a)):
        total += abs(a[i]-a[j])

print(total)
