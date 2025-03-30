import heapq


def dijkstra(start):
    pq = [start]
    directions = [(-1,0), (1,0), (0, -1), (0, 1)]
    dists = [[int(21e8)] * N for _ in range(N)]
    dists[0][0] = 0 # 시작지점
    while pq:
        dist, r, c = heapq.heappop(pq)
        if dists[r][c] < dist: # 만약 최소 가중치가 현재 가중치보다 낮으면
            continue
        for d in directions: # 4방향 탐색
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < N:
                next_dist = dists[r][c] + arr[nr][nc]
                if next_dist >= dists[nr][nc]:
                    continue
                if nr == N-1 and nc == N-1:
                    return next_dist
                dists[nr][nc] = next_dist
                heapq.heappush(pq,(next_dist, nr, nc))
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N 은 지도의 크기
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input())))
    start = (0, 0, 0) # dist, 좌표
    result = dijkstra(start)
    print(f'#{tc} {result}')
