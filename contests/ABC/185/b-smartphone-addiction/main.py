if __name__ == '__main__':
    N, M, T = map(int, input().split())
    ab = [map(int, input().split()) for _ in range(M)]
    a_list, b_list = [list(i) for i in zip(*ab)]

    answer = 'Yes'
    N0 = N
    t = 0
    for i in range(M):
        used = a_list[i]-t
        N -= used
        t = a_list[i]
        # print('Used', N)
        if N <= 0:
            answer = 'No'
            break
        charged_time = b_list[i]-t
        for _ in range(charged_time):
            if N >= N0:
                break
            N += 1
        # print('Charged', N)
        t = b_list[i]

    last_used = T-b_list[M-1]
    N -= last_used
    # print('N0', N0)
    # print('LastUsed', N)
    if N <= 0:
        answer = 'No'
    print(answer)
