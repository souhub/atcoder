n = int(input())
points = []
cnt = 0

for _ in range(n):
    point = list(map(int, input().split()))
    points.append(point)

for i in range(n-2):
    A = [points[i][0], points[i][1]]
    for j in range(i+1, n-1):
        B = [points[j][0], points[j][1]]
        if A[0] == B[0]:
            for k in range(j+1, n):
                C = [points[k][0], points[k][1]]
                if C[0] == A[0]:
                    print('Yes')
                    exit()
        elif A[1] == B[1]:
            for k in range(j+1, n):
                C = [points[k][0], points[k][1]]
                if C[1] == A[1]:
                    print('Yes')
                    exit()
        else:
            a1 = (A[1]-B[1])/(A[0]-B[0])
            b1 = B[1]-a1*B[0]
            for k in range(j+1, n):
                C = [points[k][0], points[k][1]]
                if B[0] == C[0]:
                    break
                a2 = (B[1]-C[1])/(B[0]-C[0])
                b2 = B[1]-a2*B[0]
                if a1 == a2 and b1 == b2:
                    print('Yes')
                    exit()

print('No')
