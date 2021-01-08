n = int(input())

ans = []

for j in range(1, n+1):
    for i in range(len(str(j))):
        if str(j)[i] == '7':
            ans.append(j)

    oj = oct(j)
    for i in range(len(str(oj))):
        if str(oj)[i] == '7':
            ans.append(j)


print(n-len(set(ans)))
