s = input()
p = input()

loop_s = s+s

if loop_s.find(p) == -1:
    print('No')
else:
    print('Yes')
