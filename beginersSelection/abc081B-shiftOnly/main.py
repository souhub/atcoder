# Input the values
N = int(input())
A = list(map(int, input().split()))

# Algorithm
cnt = 0
while all(i % 2 == 0 for i in A):
    A = [i/2 for i in A]
    cnt += 1

# Output the answer
print(cnt)
