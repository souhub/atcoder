n, s, d = map(int, input().split())
is_damaged = False
# x, y = [], []
for _ in range(n):
    x, y = map(int, input().split())
    if x < s and y > d:
        is_damaged = True
        break
    else:
        continue
    # x.append(xi)
    # y.append(yi)
# for i in range(n):


if is_damaged:
    print('Yes')
else:
    print('No')
