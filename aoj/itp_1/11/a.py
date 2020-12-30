dice = list(map(int, input().split()))

dirs = input()

for i in range(len(dirs)):
    if dirs[i] == 'E':
        dice = (dice[3], dice[1], dice[0], dice[5], dice[4], dice[2])
    elif dirs[i] == 'N':
        dice = (dice[1], dice[5], dice[2], dice[3], dice[0], dice[4])
    elif dirs[i] == 'S':
        dice = (dice[4], dice[0], dice[2], dice[3], dice[5], dice[1])
    elif dirs[i] == 'W':
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    else:
        print('ERROR')
        exit()

print(dice[0])
