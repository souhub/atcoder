n = int(input())
a = []
b = []
total1 = float('inf')
for _ in range(n):
    tmp_a, tmp_b = map(int, input().split())
    tmp_total = tmp_a+tmp_b
    if total1 > tmp_total:
        total1 = tmp_total
    a.append(tmp_a)
    b.append(tmp_b)
# I coudn't solve it
