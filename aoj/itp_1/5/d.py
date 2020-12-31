n = int(input())

ans = []

for i in range(1, n+1):
    if i % 3 == 0:
        ans.append(i)

    si = str(i)

    for j in range(len(si)):
        if si[j] == '3':
            ans.append(int(si))

print('', *set(ans))
