

def find_next(r, c, can_cut, cnt):
    global max_length
    destination = [(-1, 0), (1, 0), (0, -1), (0, 1)] #상 하 좌 우


    for d in destination:  # 상하좌우 다 보기
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < N and 0 <= nc < N:  # 갈 수 있는 범위라면
            if arr[nr][nc] < arr[r][c]:
                visited[nr][nc] = 1
                find_next(nr, nc, can_cut, cnt + 1)
                visited[nr][nc] = 0
            else:
                if can_cut == 1:  # 퍼낼 수 있을 떄,
                    for i in range(1, K + 1):
                        if arr[nr][nc] - i < arr[r][c] and visited[nr][nc] ==0:  # 현재 지점보다 낮아야하니깐
                            origin_h = arr[nr][nc]
                            arr[nr][nc] -= i
                            visited[nr][nc] = 1
                            find_next(nr, nc, 0, cnt + 1)
                            visited[nr][nc] = 0
                            arr[nr][nc] = origin_h  # 파낸 것 복구

    if max_length < cnt:
        max_length = cnt
    return

def dfs():
    global max_length
    start = [] # 시작할 수 있는 최대 봉우리
    for i in range(N): # 전체 순회하면서 최대 봉우리 찾아주기
        for j in range(N):
            if arr[i][j] == max_h:
                start.append((i, j))
    for start_node in start:
        start_r , start_c = start_node
        visited[start_r][start_c] = 1
        find_next(start_r, start_c, 1, 1)
        visited[start_r][start_c] = 0

    return max_length

# 1.일단 최대한 높은 지형 찾기 2. 갈 수 있는 곳 다 깎아보기
T =int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # N 은 지도 한 변의 길이, K는 팔 수 있는 깊이
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_h = 0
    max_length = 0
    visited= [[0] * N for _ in range(N)]
    for row in arr:
        max_h = max(max_h, max(row)) # 최대값 찾아주기
    # print(max_h)
    print(f'#{tc} {dfs()}')
'''
1
3 2       
1 2 1     
2 1 2
1 2 1
'''