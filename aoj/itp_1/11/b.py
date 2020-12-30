import itertools

dice = list(map(int, input().split()))

q = int(input())

oprs = []

for _ in range(q):
    oprs.append(list(map(int, input().split())))

for opr in oprs:
    if opr == [dice[1], dice[2]] or opr == [dice[2], dice[4]] or opr == [dice[3], dice[1]] or opr == [dice[4], dice[3]]:
        print(dice[0])
    elif opr == [dice[0], dice[3]] or opr == [dice[2], dice[0]] or opr == [dice[3], dice[5]] or opr == [dice[5], dice[2]]:
        print(dice[1])
    elif opr == [dice[0], dice[1]] or opr == [dice[1], dice[5]] or opr == [dice[4], dice[0]] or opr == [dice[5], dice[4]]:
        print(dice[2])
    elif opr == [dice[0], dice[4]] or opr == [dice[1], dice[0]] or opr == [dice[4], dice[5]] or opr == [dice[5], dice[1]]:
        print(dice[3])
    elif opr == [dice[0], dice[2]] or opr == [dice[2], dice[5]] or opr == [dice[3], dice[0]] or opr == [dice[5], dice[3]]:
        print(dice[4])
    elif opr == [dice[1], dice[3]] or opr == [dice[2], dice[1]] or opr == [dice[3], dice[4]] or opr == [dice[4], dice[2]]:
        print(dice[5])
    else:
        print('ERROR')
        exit()
