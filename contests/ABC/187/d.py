vote_a = []
vote_t = []

n = int(input())

for i in range(n):
    vote = list(map(int, input().split()))
    vote_a.append(vote[0])
    vote_t.append(vote[1])

sum_a = sum(vote_a)
sum_t = sum(vote_t)

# d=[2*a+t for a,t in zip(vote_a,vote_t)]
max_d = 2*vote_a[0]+vote_t[0]

cnt = 0
index = -1
while True:
    for i in range(1, n):
        if max_d < 2*vote_a[i]+vote_t[i]:
            max_d = 2*vote_a[i]+vote_t[i]
            index = i
    sum_t += vote_t[index]
    sum_a -= vote_a[index]
    cnt += 1
    if sum_t > sum_a:
        print(cnt)
        break
