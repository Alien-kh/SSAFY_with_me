import sys
input = sys.stdin.readline

# 특정 거리의 도시 찾기

def solve(start, k):
    queue = [(start, 0)]  # (현재 위치, 거리)
    visited[start] = 1
    result = []

    while queue:
        now, dist = queue.pop(0)

        # 목표 거리 도달 시 결과 저장
        if dist == k:
            result.append(now)

        # 인접 도시 탐색
        for next_pos in graph[now]:
            if not visited[next_pos]:
                visited[next_pos] = 1
                queue.append((next_pos, dist + 1))

    if result:
        for city in sorted(result):
            print(city)
    else:
        print(-1)

# 입력부
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

# BFS 탐색 시작
solve(X, K)
