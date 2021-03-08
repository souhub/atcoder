def stdin(n):
    a = []
    b = []
    for i in range(n):
        tmp_a, tmp_b = map(int, input().split())
        a.append(tmp_a)
        b.append(tmp_b)
    return a, b


def main(a, b):
    n = len(a)
    total = float('inf')
    for i in range(n):
        for j in range(n):
            if i == j:
                total = min(total, a[i]+b[j])
            else:
                total = min(total, max(a[i], b[j]))
    return total


if __name__ == '__main__':
    n = int(input())
    a, b = stdin(n)
    total = main(a, b)
    print(total)
