s = input()
is_diff = True
for i in range(len(s)):
    if i % 2 == 0:
        if not s[i].islower():
            is_diff = False
            break
    else:
        if not s[i].isupper():
            is_diff = False
            break

if is_diff:
    print('Yes')
else:
    print('No')
