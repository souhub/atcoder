import math

ans = []

while True:
    try:
        n = int(input())

        s = list(map(float, input().split()))

        sum_s = 0

        for si in s:
            sum_s += si

        m = sum_s/n

        sum_sm = 0

        for si in s:
            sum_sm += (si-m)**2

        aa = sum_sm/n

        ans.append(aa)

    except:
        break

for i in ans:
    print(math.pow(i, 1/2))
