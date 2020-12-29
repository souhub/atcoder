n, x = map(int, input().split())
s = input()

for i in range(0, n):
    if s[i] == 'o':
        x += 1
    else:
        if x == 0:
            continue
        else:
            x -= 1
print(x)
