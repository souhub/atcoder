# Dynamic Programming

N = int(input())

a = list(map(int, input().split()))

dp = [float('-inf') for _ in range(len(a))]

dp[0] = 0
dp[1] = abs(a[1]-a[0])

for n in range(2, len(a)):
    dp[n] = min(dp[n-2]+abs(a[n]-a[n-2]), dp[n-1]+abs(a[n]-a[n-1]))

print(dp[len(a)-1])
