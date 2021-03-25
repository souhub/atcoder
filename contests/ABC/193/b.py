n = int(input())
ans = float('inf')
for i in range(n):
    a, p, x = map(int, input().split())
    saled_products = a
    if x > saled_products and p < ans:
        ans = p
if ans == float('inf'):
    ans = -1
print(ans)
