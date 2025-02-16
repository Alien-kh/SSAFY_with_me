def solve(n, m, arr):
    dr = [-1,-1,-1,0,1,1,1,0] # 맨 왼쪽 위 부터 시계 방향
    dc = [-1,0,1,1,1,0,-1,-1]
    total_count = 0 # 착률할 수 있는 지점 수
    for r in range(n):
        for c in range(m):
            count = 0 # 촬영 가능한 수 세기
            v = arr[r][c] # 현재 착륙한 지점
            for d in range(8): # 8방향 탐색
                nr = r +dr[d]
                nc = c +dc[d]
                if 0 <= nr < n and 0 <= nc <m and v > arr[nr][nc]: # v보다 작고, arr범위 안에 있으면
                        count +=1 # 촬영 가능 한 수 up
            if count>= 4: # 만약 4곳이상이면
                total_count+=1 # 착륙장소 up
    return total_count

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split()))for _ in range(N)]
    result = solve(N, M, arr)
    print(f'#{tc} {result}')