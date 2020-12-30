s = input()

q = int(input())

cmds = []

for i in range(q):
    cmd = list(map(str, input().split()))
    cmds.append(cmd)

for cmd in cmds:
    a = int(cmd[1])
    b = int(cmd[2])
    if cmd[0] == 'print':
        print(s[a:b+1])
    elif cmd[0] == 'reverse':
        word = s[a:b+1]
        r_word = word[::-1]
        s = s[:a]+r_word+s[b+1:]
    elif cmd[0] == 'replace':
        s = s[:a]+cmd[3]+s[b+1:]
    else:
        print('ERROR')
