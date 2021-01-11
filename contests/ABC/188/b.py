n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
total = 0
while i < n:
    inner_product = a[i]*b[i]
    total += inner_product
    i += 1
if total == 0:
    print('Yes')
else:
    print('No')
