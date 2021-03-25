import math

N = int(input())
nums = set()
for a in range(2, int(math.sqrt(N))+1):
    x = a*a
    while x <= N:
        nums.add(x)
        x *= a
print(N-len(nums))
