points = []

n = int(input())

for i in range(n):
    point = list(map(int, input().split()))
    points.append(point)

cnt = 0

for j in range(n):
    for k in range(n):
        dx = points[j][0]-points[k][0]
        dy = points[j][1]-points[k][1]

        if dx == 0:
            break

        a = dy/dx
        if abs(a) <= 1:
            cnt += 1

print(cnt)
