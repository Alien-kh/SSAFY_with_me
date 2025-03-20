import heapq
INF = int(21e8)

def dijkstra():
    pq = [(0, 0, 0)] # 시작 연료 0 , 좌표 0, 0
    dists = [[INF] * N for _ in range(N)]
    dists[0][0] = 0 # 시작은 항상  0
    destination = [(0,1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상
    while pq:
        dist, r, c  = heapq.heappop(pq) # 가는데 쓴 연료, 좌표

        # 이미 더 작은 경로 온 적 있으면
        if dists[r][c] < dist:
            continue

        for d in destination:
            nr = r + d[0]
            nc = c + d[1]
            if 0 <= nr < N and 0 <= nc < N:
                new_h = max(0, arr[nr][nc] - arr[r][c]) #높이 차이를 구하기 위해서 다음 높이 - 현재 높이
                new_dist = dist + 1 + new_h # 한 칸 이동 + 높이가 있다면 높이만큼
                # 이미 같은 가중치거나, 더 작은 가중치로 온 적이 있으면 넘어가기
                if dists[nr][nc] <= new_dist:
                    continue
                dists[nr][nc] = new_dist
                heapq.heappush(pq, (new_dist, nr, nc))
    return dists[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = dijkstra()
    print(f'#{tc} {result}')