s = ''

while True:
    try:
        s += input().lower()
    except:
        break

alps = 'abcdefghijklmnopqrstuvwxyz'

for j in range(len(alps)):
    cnt = s.count(alps[j])
    print('{} : {}'.format(alps[j], cnt))
