sx, sy, gx, gy = map(int, input().split())

y = sy / (sy + gy)
x = sx + (gx-sx) * y

print(x)

# Ref: https://yamakasa.net/atcoder-abc-183-b/
