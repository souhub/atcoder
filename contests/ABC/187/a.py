a, b = map(str, input().split())

sum_a, sum_b = 0, 0

for i in range(len(a)):
    sum_a += int(a[i])

for i in range(len(b)):
    sum_b += int(b[i])

if sum_a > sum_b:
    print(sum_a)
else:
    print(sum_b)
