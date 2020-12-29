s = input()

ans = ''

for i in range(len(s)):
    if s[i].isupper():
        ans += s[i].lower()
    elif s[i].islower():
        ans += s[i].upper()
    else:
        ans += s[i]

print(ans)
