sec = int(input())

h = sec//60**2

m = (sec % 60**2)//60

s = (sec % 60**2) % 60

print('{0}:{1}:{2}'.format(h, m, s))
