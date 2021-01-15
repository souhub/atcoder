total = 0

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    m = b-a+1
    avg = (a+b)/2
    sub_total = avg*m
    total += sub_total

print(int(total))
