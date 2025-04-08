# 백준 제출용 import. 시간 차이일 뿐 밑의 코드대로 공부하자.
import sys
input = sys.stdin.readline

# 방향 없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램

N, M = map(int, input().split())    # 정점, 간선 수

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())  # 시작점, 끝 점 정보 받기
    graph[s].append(e)
    graph[e].append(s)

# 방문 여부 확인!!!!
visited = [0] * (N+1)


def dfs(node):
    stack = [node]
    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = 1
            for adj in graph[now]:
                if not visited[adj]:
                    stack.append(adj)


# 연결 요소 카운트
count = 0
for i in range(1, N+1):
    if visited[i] == 0: # 시작하지 않은 정점에서 DFS 시작.
        dfs(i)
        count += 1

print(count)
