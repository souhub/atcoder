x1, y1, x2, y2 = map(float, input().split())

dx = x1-x2
dy = y1-y2

print(pow(dx**2+dy**2, 0.5))
