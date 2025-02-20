from collections import deque

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9: # 시작 위치 찾기
            x = i
            y = j
            arr[i][j] = 0

shark_size = 2 # 상어 사이즈
now_eat = 0 # 현재 먹은 물고기 // 만약 사이즈랑 값이 같다면 0 초기화하고 사이즈 +1 해줘야함
def bfs(x,y):
    queue = deque()
    cnt = 0
    queue.append((x,y)) # 거리까지 포함해서 큐에 집어넣음

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y = queue.popleft() # 좌표랑 거리를 꺼냄
        visited = [[-1] * N for _ in range(N)]
        visited[x][y] = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= N or ny >= N: # 범위 밖이면 제외
                continue
            
            if arr[nx][ny] < shark_size and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
    return visited

def solve(visited):
    a,b = 0,0
    min_distance = 10000000
    for i in range(N):
        for j in range(N):
            if visited[i][j] != -1 and 1 <= arr[i][j] < shark_size:
                min_distance = visited[i][j]
                a,b = i,j
    if min_distance == 10000000:
        return False
    else:
        return x,y,min_distance
    
answer = 0
food = 0

while True:
    result = solve(bfs(x,y))

    if not result:
        print(answer)
        break
    else:
        x,y = result[0],result[1]
        answer += result[2]
        arr[x][y] = 0
        food += 1

    if food >= shark_size:
        shark_size += 1
        food = 0





