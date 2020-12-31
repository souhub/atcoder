a, b = map(int, input().split())

if a > b:
    large, small = a, b
else:
    large, small = b, a

while True:
    if a == b:
        gcd = a
        break

    remainder = large % small

    large = small

    small = remainder

    if remainder == 0:
        break

    gcd = remainder

print(gcd)
