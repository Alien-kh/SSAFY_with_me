def dfs(s, visited):
    global max_value, weight_s, value_s, last_num

    visited[s] = 1  # 시작 노드 방문 처리  

    # 현재 무게 초과 시 되돌아감
    if weight_s + s > M:
        weight_s -= last_num  # 마지막에 추가된 무게 빼기
        if max_value < value_s:
            max_value = value_s
        value_s -= item_dict[s]  # 가치를 감소
        return

    weight_s += s
    value_s += item_dict[s]

    for i in graph[s]:
        if not visited[i]:  # 방문하지 않은 노드 탐색
            last_num = i
            dfs(i, visited)

    # 백트래킹 (되돌아가기)
    weight_s -= s
    value_s -= item_dict[s]
    visited[s] = 0 


N, M = map(int, input().split())
W = []
V = []
item_dict = {}

for _ in range(N):
    a, b = map(int, input().split())
    W.append(a)
    V.append(b)
    item_dict[a] = b

W.sort()
E = max(W)

# 그래프 초기화 (연결 방식 수정)
graph = {w: [] for w in W}
for i in range(len(W)):
    for j in range(i + 1, len(W)):  # i와 j가 같은 경우를 방지
        graph[W[i]].append(W[j])

max_value = 0
weight_s = 0
value_s = 0

for i in W:
    visited = {w: 0 for w in W}  # 방문 배열 초기화
    dfs(i, visited)

print(max_value)
