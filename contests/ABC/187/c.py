# C - 1-SAT /

s1 = []  # the word of s1 has '!'
s2 = []  # does't have '!'
match = False

n = int(input())

for i in range(n):
    ss = input()
    if ss[0] == '!':
        s1.append(ss)
    else:
        s2.append(ss)

s1 = sorted(set(s1))
s2 = sorted(set(s2))

for ss1, ss2 in zip(s1, s2):
    if ss1 == '!'+ss2:
        print(ss2)
        match = True
        break

if not match:
    print('satisfiable')
