N = int(input()) # 컴퓨터의 수

L = int(input()) # 연결된 선

# 경로를 보여주는 arr 배열.
arr = [[] for _ in range(N + 1) ]

for _ in range(L):
    # 연결 정보를 받아서, 언패킹.
    a, b = map(int, input().split())
    
    # 서로 연결된 곳 배열에 표시.
    arr[a].append(b)
    arr[b].append(a)


# *** 중요! BFS 방식 -> Queue ***
queue = [1] # 1번 컴퓨터가 항상 웜 바이러스에 걸림.
visited = [0] * (N + 1)
visited[1] = 1  # 1번 컴퓨터 감염 상태
count = 0   # 1번 컴퓨터를 제외하고 감염된 컴퓨터 세기

while queue:
    current = queue.pop(0)

    for next in arr[current]:   # 현재 노드(컴퓨터)와 연결된 모든 노드 확인
        if not visited[next]:   # 아직 방문하지 않은 컴퓨터라면
            visited[next] = 1   # 방문 처리. -> 중복 방지.
            queue.append(next)  # queue에 추가해서 탐색 할 수 있게 만듬.
            count += 1          # 감염된 컴퓨터 수 증가.

print(count)