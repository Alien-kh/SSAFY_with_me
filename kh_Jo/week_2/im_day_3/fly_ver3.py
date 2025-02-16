def solve():
    # 상하좌우 dr/dc1
    dr1 = [-1, 1, 0, 0]
    dc1 = [0, 0 ,-1, 1]
    # 오른쪽 위, 아래 왼쪽 아래, 위
    max_v = -21e8
    dr2 = [-1, 1, 1, -1]
    dc2 = [1, 1, -1, -1]
    for r in range(N): # 모든 arr 칸 기준으로 + 계산
        for c in range(N):
            sum_v = 0
            sum_v += arr[r][c] # 자기 자신 더해주기
            for a in range(1,M): # 1부터 시작해서 M칸까지
                for d in range(4): # 4방향
                    nr1 = r + dr1[d] * a
                    nc1 = c + dc1[d] * a
            # 유효한 범위 이내라면 더해주기
                    if 0<= nr1 < N and 0<= nc1 < N:
                        sum_v += arr[nr1][nc1]

            if max_v < sum_v:
                max_v = sum_v

    for r in range(N): # 모든 arr 칸 기준으로 + 계산
        for c in range(N):
            sum_v = 0
            sum_v += arr[r][c] # 자기 자신 더해주기
            for a in range(1,M): # 1부터 시작해서 M칸까지
                for d in range(4): # 4방향
                    nr2 = r + dr2[d] * a
                    nc2 = c + dc2[d] * a
            # 유효한 범위 이내라면 더해주기
                    if 0<= nr2 < N and 0<= nc2 < N:
                        sum_v += arr[nr2][nc2]
            if max_v < sum_v:
                max_v = sum_v
    return max_v


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    result = solve()

    print(f'#{tc} {result}')