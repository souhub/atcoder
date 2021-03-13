n = int(input())
cnt = 0
if n >= 10**3:
    cnt += n-10**3+1
if n >= 10**6:
    cnt += n-10**6+1
if n >= 10**9:
    cnt += n-10**9+1
if n >= 10**12:
    cnt += n-10**12+1
if n >= 10**15:
    cnt += n-10**15+1

print(cnt)
