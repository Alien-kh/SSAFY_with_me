from collections import deque
'''
그람을 얻은 후부터는 벽을 다 부수고 이동 가능
visited를 2차원으로 만든 후 얻기 전과 얻은 후 구분
'''
def bfs():
    queue = deque()
    queue.append((0,0,0)) # row , col , 상태, 거리
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x,y,state = queue.popleft()
        if x == N-1 and y == M-1:
            continue
        if visited[x][y][state] == T+1:
            continue
        for k in range(4):
            nx = x + dx[k]  # 델타
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: # 범위 밖이면 다음 루프로
                continue

            if state == 0: # 검 얻기 전
                if graph[nx][ny] != 1 and not visited[nx][ny][state]:
                    if graph[nx][ny] == 2: # 검 뽑을떄
                        queue.append((nx,ny,1)) # 검 뽑으면 상태를 1로 바꿈
                        visited[nx][ny][1] = visited[x][y][0] + 1
                    else: # 그냥 지나갑니다
                        queue.append((nx,ny,0))
                        visited[nx][ny][0] = visited[x][y][0] + 1
            elif not visited[nx][ny][state]: # 검 얻은 상태
                    queue.append((nx,ny,1))
                    visited[nx][ny][1] = visited[x][y][1] + 1
    return 1
N,M,T = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)]  for _ in range(N)]
bfs()
min_result = 1e9

for i in visited[N-1][M-1]:
    if i and min_result > i:
        min_result = i

if min_result == 1e9 or min_result > T:
    print('Fail')
else:
    print(min_result)