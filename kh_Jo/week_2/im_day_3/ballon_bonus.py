def solve():
    # 상하좌우 델타
    dr = [-1, 1, 0, 0] #
    dc = [0, 0, -1, 1]
    Max_num = -21e8 # 최대값
    Min_num = 21e8 # 최솟값
    for r in range(N):  #격자퐌
        for c in range(N):
            sum_v = 0 # 추후에 비교할 점수의 합
            sum_v = arr[r][c] # 자기 자신을 포함해서 나아가면서 점수를 더해야 하기에 자기 점수 더해주기
            for a in range(1, N): # 최대 N-1칸 까지 나아갈 수 있으니깐
                for d in range(4): # 4방향
                    nr = r + dr[d] * a
                    nc = c + dc[d] * a
                    if 0 <= nr < N and 0 <= nc < N: # 인덱스가 가능한 위치들만
                        sum_v += arr[nr][nc]
            # 반복이 끝난후 최종 합 비교
            if Max_num < sum_v:
                Max_num = sum_v

            if Min_num > sum_v:
                Min_num = sum_v

    return Max_num - Min_num



T = int(input())    #스테이지 개수
for tc in range(1, T+1):
    N = int(input())    # 격자의 크기
    arr = []
    for _ in range(N):  # 격자의 크기 만큼 반복
        arr.append(list(map(int, input().split())))

    result = solve()
    print(f'#{tc} {result}')