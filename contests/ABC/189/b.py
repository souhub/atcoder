n, x = map(int, input().split())


def main(n, x):
    total = 0.0
    ans = -1
    for i in range(n):
        v, p = map(int, input().split())
        total += v*p
        # 整数のみで計算するために100xにする
        if total > 100*x:
            ans = i+1
            break
    return ans


result = main(n, x)
print(result)
