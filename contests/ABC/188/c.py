# トーナメント左半分で1番高い人と右半分の1番の人を求めれば良い
n = int(input())
a = list(map(int, input().split()))
if n == 1:
    if a[0] > a[1]:
        second_place = 1
    else:
        second_place = 0
else:
    center_index = len(a)//2
    left_side = [a[i] for i in range(0, center_index)]
    right_side = [a[i] for i in range(center_index, len(a))]
    left_highest_score = max(left_side)
    right_highest_score = max(right_side)
    second_highest_score = min(left_highest_score, right_highest_score)
    second_place = a.index(second_highest_score)
print(second_place+1)
