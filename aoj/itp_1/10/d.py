n = int(input())

xn = list(map(int, input().split()))

yn = list(map(int, input().split()))

pn = [1, 2, 3]

for p in pn:
    print(pow(sum(pow(abs(x-y), p) for x, y in zip(xn, yn)), 1/p))

print(max(abs(x-y) for x, y in zip(xn, yn)))
