def solve(arr):
    # 상하좌우로 값을 구할 것이기에 델타 설정
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 최댓값 설정
    max_v = -21e8
    for r in range(N):
        for c in range(M):
            sum_v = 0
            sum_v += arr[r][c]
            for d in range(4):
                for a in range(1, arr[r][c]+1): # 가운데 개수 만큼 추가로 터지니깐
                    nr = r + dr[d] * a
                    nc = c + dc[d] * a
                    if 0 <= nr < N and 0 <= nc < M:
                        sum_v += arr[nr][nc]
                # 다 더해준 뒤에 각 항별로 최댓값 비교
            if max_v < sum_v:
                max_v = sum_v
    return max_v



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 은 줄 M 은 줄마다 풍선 개수
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = solve(arr)

    print(f'#{tc} {result}')