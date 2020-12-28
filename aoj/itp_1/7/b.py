import itertools

cnts = []

while True:
    cnt = 0

    lc = list(map(int, input().split()))

    max = lc[0]
    target = lc[1]

    if max == target == 0:
        break

    numbers = []
    for i in range(1, max+1):
        numbers.append(i)

    combs = itertools.combinations(numbers, 3)

    for comb in combs:
        sum = 0
        for i in comb:
            sum += i

        if sum == target:
            cnt += 1

    cnts.append(cnt)

for cnt in cnts:
    print(cnt)
