#풍선팡 2
T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 격자 크기 N x M
    grid = [list(map(int, input().split())) for _ in range(N)]  # 풍선 격자 데이터

    max_flower = 0  # 최댓값 저장 변수

    # 상하좌우 방향 탐색을 위한 리스트
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 모든 위치에서 풍선을 터트려본다.
    for x in range(N):
        for y in range(M):
            flower_count = grid[x][y]  # 현재 풍선의 꽃가루 개수

            # 상하좌우 터지면서 꽃가루 추가
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < M:  # 범위 체크
                    flower_count += grid[nx][ny]

            # 최댓값 갱신
            if flower_count > max_flower:
                max_flower = flower_count

    # 결과 출력
    print(f"#{tc} {max_flower}")
