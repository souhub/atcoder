# # Input the values.
N, A, B = map(int, input().split())

# Define the variables.
sumsum = 0

# # Algorithm
for n in range(1, N+1):
    sum = 0
    tmp = n
    for i in range(5):
        d = 10**(4-i)
        r = int(n/d)
        sum += r
        n -= r*10**(4-i)
        # print(d, r, sum, n)

    if A <= sum <= B:
        sumsum += tmp

    n -= 1

# # Output
print(sumsum)
