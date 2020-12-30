w = input()
t = []

while True:
    col = list(map(str, input().split()))
    if col[0] == 'END_OF_TEXT':
        break
    for s in col:
        t.append(s.lower())

print(t.count(w))
