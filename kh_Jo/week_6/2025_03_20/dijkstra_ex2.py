# 다익스트라
'''
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

def dijkstra(S, G):
    distance = [0xffffff]* (V+1)# 시작 정점에서 다른 정점까지 가는 비용
    distance[S] = 0
    checked = set() # 비용이 확정된 정점의 모음
    # 모든 정점까지 가는 비용 계산
    while len(checked) < V:
        min_v = -1
        min_distance = 0xffffff
        # 최소 비용으로 갈 수 있는 정점 선택
        for i in range(V):
            if i not in checked and distance[i] < min_distance:
                min_distance = distance[i]
                min_v = i
        checked.add(min_v)
        # 선택된 정점을 거쳐서 갈 수 있는 비용 수정
        for i in range(V+1):
            # 시작 정점에서 min_v를 거쳐서 i로 가는 비용
            # 시작 정점에서 min_v로 가는 비용 : distance[min_v]
            g[min_v][i] + distance[min_v]
            # 원래 내가 알고 있던 i로 가는 비용 distance[i]
            if i not in checked  and g[min_v][i] and g[min_v][i] + distance[min_v] < distance[i]:
                distance[i] = g[min_v][i] + distance[min_v]
    return distance[-1]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    g = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b, w = map(int,input().split())
        g[a][b] = w # 반대는 없음, 유향그래프
    result = dijkstra(0, V)
    print(f'#{tc} {result}')
# dijkstra(0, 5)