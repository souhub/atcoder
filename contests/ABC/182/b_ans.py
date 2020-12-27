from collections import Counter
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = []
for i in range(n):
    for j in range(2, a[n-1]+1):
        if a[i] % j == 0:
            ans.append(j)

print(Counter(ans).most_common()[0][0])

# わからない
