# Prim 알고리즘을 이용해 최소 신장 트리(MST)의 가중치 합을 구하는 함수
def prim(V, g):
    weights = [0xfffffff] * V  # 각 정점까지의 최소 가중치, 초기값은 무한대
    weights[0] = 0  # 시작 정점의 가중치는 0으로 설정
    MST = set()  # MST에 포함된 정점들을 저장하는 집합
    total_weight = 0  # 최소 신장 트리의 총 가중치

    # 모든 정점이 MST에 포함될 때까지 반복
    while len(MST) < V:
        min_w = 0xffffff  # 현재 확인 중인 최소 가중치
        min_v = -1  # 최소 가중치를 가진 정점의 번호

        # 아직 MST에 포함되지 않은 정점 중 가중치가 가장 작은 정점 선택
        for i in range(V):
            if i not in MST and weights[i] < min_w:
                min_w = weights[i]
                min_v = i

        MST.add(min_v)  # 선택된 정점을 MST에 추가
        total_weight += min_w  # 최소 가중치를 총합에 더함

        # 선택된 정점과 연결된 정점들의 가중치 업데이트
        for i in range(V):
            if i not in MST and g[min_v][i] < weights[i]:
                weights[i] = g[min_v][i]

    return total_weight  # MST의 총 가중치 반환


T = int(input())
for tc in range(1, T + 1):
    V_input, E = map(int, input().split())  # V_input: 정점 수(사용 안 함), E: 간선 수
    edges = []  # 간선 정보를 저장할 리스트
    max_v = 0  # 정점 번호의 최대값을 저장

    # 간선 정보 입력
    for _ in range(E):
        a, b, w = map(int, input().split())  # a, b: 정점 번호, w: 가중치
        edges.append((a, b, w))
        max_v = max(max_v, a, b)  # 최대 정점 번호 업데이트

    V = max_v + 1  # 정점 개수: 최대 정점 번호 + 1 (0번부터 시작하기 때문)

    # 인접 행렬 초기화 (무한대 값으로 초기화)
    g = [[0xffffffff] * V for _ in range(V)]

    # 간선 정보를 인접 행렬에 저장
    for a, b, w in edges:
        g[a][b] = w
        g[b][a] = w  # 무방향 그래프이므로 양방향 저장

    result = prim(V, g)
    print(f'#{tc} {result}')
