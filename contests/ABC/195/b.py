import math

a, b, w = map(int, input().split())
w *= 1000
min_mikan = math.ceil(w/b)
max_mikan = math.floor(w/a)
if min_mikan > max_mikan:
    ans = 'UNSATISFIABLE'
    print(min_mikan, max_mikan)
else:
    mikan_list = [str(min_mikan), str(max_mikan)]
    ans = ' '.join(mikan_list)
print(ans)
