def maze(r, c):
    stack = [(r, c)]
    while stack:
        x, y = stack.pop()
        
        # 도착 지점(3)을 찾으면 1 반환
        if arr[x][y] == '3':
            return 1
        
        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nr, nc = x + d[0], y + d[1]
            
            # 미로 범위 내에서 이동 가능하고 아직 방문하지 않은 곳
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] != '1':
                visited[nr][nc] = 1
                stack.append((nr, nc))

    return 0  # 도착지점에 도달할 수 없으면 0 반환

T = int(input())  # 테스트 케이스 개수
for tc in range(1, T + 1):
    N = int(input())  # 미로의 크기
    arr = [list(input().strip()) for _ in range(N)]  # 미로 입력 받기
    visited = [[0] * N for _ in range(N)]  # 방문 여부 배열

    # 출발점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start = (i, j)
                visited[i][j] = 1  # 출발점은 방문형태로.
    
    # 결과 출력
    print(f"#{tc} {maze(*start)}")