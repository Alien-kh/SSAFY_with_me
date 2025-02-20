from collections import deque
 
def bfs(x,y): # bfs 알고리즘
    queue = deque()
    queue.append((x,y)) # 시작지점을 큐에 담음

    while queue: # 큐가 있을떄 까지 존재 -> 통로가 없으면 종료됨
        x,y = queue.popleft() # 시작 지점을 큐에서 꺼내고 x,y로 변수 설정

        for k in range(4): # 델타로 상하좌우 탐색
            nx = x + dx[k]
            ny = y + dy[k]

            if nx >= N or ny >= N or nx < 0 or ny < 0: # 범위 밖이면 다음으로
                continue
            if arr[nx][ny] == 1: # 벽이면 다음으로
                continue

            if arr[nx][ny] == 3: # 도착지점이면 1 리턴
                return 1
            
            if arr[nx][ny] == 0: # 통로라면 큐에 좌표를 담고 그 지점을 1로 바꿔서 방문처리해줌
                queue.append((nx,ny))
                arr[nx][ny] = 1
    return 0 

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().rstrip())) for _ in range(N)]

    dx = [-1,1,0,0] # 델타 설정
    dy = [0,0,-1,1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2: # 출발점 탐색
                x = i
                y = j
                break

    print(f'#{test_case}',bfs(x,y))