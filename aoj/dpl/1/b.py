value, weight = [], []
N, W = map(int, input().split())
for i in range(N):
    x, y = map(int, input().split())
    value.append(x)
    weight.append(y)

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
print(dp)

# for j in range(N):
#     for k in range(W+1):
#         if k < w[j]:
#             dp[j+1][k] = dp[j][k]
#         else:
#             dp[j+1][k] = max(dp[j][k], dp[j][k-w[j]]+v[j])

# print(dp[N][W])
