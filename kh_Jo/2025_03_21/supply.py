# 전형적인 다익스트라 문제
# 1. 최단 거리를 저장할 때 dists 리스트를 이차원 리스트로 만들어야 한다.
#           -> 특정 좌표(y,x)에 갈 때 최단 거리르 저장해야 한다.
import heapq
# => 삽입 : logN / 삭제: logN - > 완전 이진 트리 => logN이 보장
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dijkstra():
    dists = [[int(21e8)] * N for _ in range(N)] # =>만약 계산결과가 21억을 넘으면 float('inf') 를 써야됨
    dists[0][0] = 0  # 시작점 초기화

    pq = [(0, 0, 0)]  # (dist - 누적거리, y, x) 형태

    while pq:
        dist, y, x = heapq.heappop(pq)

        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]

            # 범위 밖이면 continue
            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
                continue

            new_dist = dists[y][x] + graph[new_y][new_x]
            # 이미 더 작거나 같은 시간으로 온 적이 있으면 continue
            if dists[new_y][new_x] <= new_dist:
                continue

            if new_y == N - 1 and new_x == N - 1:
                return new_dist

            dists[new_y][new_x] = new_dist
            heapq.heappush(pq, (new_dist, new_y, new_x))

    return dists[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    result = dijkstra()
    print(f'#{tc} {result}')
