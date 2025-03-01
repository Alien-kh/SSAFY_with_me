# 풍선팡 문제
T = int(input())

dr = [-1,1,0,0]
dc = [0,0,-1,1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = -1

    for r in range(N):
        for c in range(M):
            sum_value = arr[r][c]
            for d in range(4):
                for a in range(1, arr[r][c]+1):
                    nr = r + dr[d] * a
                    nc = c + dc[d] * a
                    if 0 <= nr < N and 0<= nc < M:
                        sum_value += arr[nr][nc]
            max_v = max(max_v, sum_value)
    print(f"#{tc} {max_v}")
