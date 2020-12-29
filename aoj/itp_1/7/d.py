n, m, l = map(int, input().split())

a = []
b = []

for i in range(n):
    lc = list(map(int, input().split()))
    a.append(lc)

for i in range(m):
    lc = list(map(int, input().split()))
    b.append(lc)

# [a[0][0]*b[0][0] + a[0][1]*b[1][0],
#  a[0][0]*b[0][1] + a[0][1]*b[1][1],
#  a[0][0]*b[0][2] + a[0][1]*b[1][2]]


c = []
for nn in range(n):
    c_col = []
    for ll in range(l):
        c_element = 0
        for mm in range(m):
            c_element += a[nn][mm]*b[mm][ll]
        c_col.append(c_element)
    c.append(c_col)

for cc in c:
    print(*cc)
