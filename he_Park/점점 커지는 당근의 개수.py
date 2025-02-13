T = int(input())
for i in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    max_cnt = 1
    cnt = 1
    for j in range(N-1):
        if C[j] < C[j+1]:
            cnt += 1
            if max_cnt < cnt: max_cnt = cnt
        if C[j] >= C[j+1]:
            cnt = 1

    print(f'#{i} {max_cnt}')