n = int(input())

socks = list(map(int, input().split()))

cnt = 0

i = 0

while True:
    target = socks[i]

    for j in range(i+1, n):
        if target == socks[j]:
            cnt += 1
            socks.remove(socks[j])
            n -= 1
            break
    i += 1

    if i == n:
        break

print(cnt)
