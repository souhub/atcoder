# Input the values
A, B, C, X = [int(input()) for i in range(4)]
# Algorithm
cnt = 0

for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            sum = 500*a+100*b+50*c
            if sum == X:
                cnt += 1

# Output the answer
print(cnt)
