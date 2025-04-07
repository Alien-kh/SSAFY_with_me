import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

# 트리 입력 받기
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 부모 노드를 저장할 리스트
parent = [0] * (N + 1)

# 방문 여부
visited = [False] * (N + 1)

# 스택을 활용한 DFS
stack = [1]
visited[1] = True

while stack:
    node = stack.pop()
    for neighbor in graph[node]:
        if not visited[neighbor]:  # 방문하지 않은 노드라면
            parent[neighbor] = node  # 부모 저장
            visited[neighbor] = True  # 방문 체크
            stack.append(neighbor)  # 스택에 추가

# 부모 노드 출력
for i in range(2, N + 1):
    print(parent[i])
