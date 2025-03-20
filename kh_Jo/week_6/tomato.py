from collections import deque

def bfs():
    cnt = 0
    q = deque()
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                q.append((i, j, 0))  # 만약 1인 것을 찾으면 좌표 넣어주기

    destination = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
    while q:
        # print(q.popleft())
        r, c, cnt = q.popleft() # 일단 뽑고
        for d in destination:
            nr = r + d[0]
            nc = c + d[1]
            if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] ==0: # 범위 이내이고 0일 떄만
                arr[nr][nc] =1 # 토마토 숙성 해주고 다음 날로 넘기기
                q.append((nr, nc, cnt+1)) # 다음 것 +1 더해서 넣어주기
    return cnt


N, M = map(int, input().split()) # N은 가로 , M은 세로
arr = [list(map(int, input().split())) for _ in range(M)]
start = []
all_done = True
result = bfs()
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            all_done = False
            break
if all_done:
    print(result)
else:
    print(-1)