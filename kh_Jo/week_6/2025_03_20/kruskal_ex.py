'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]


# for edge in edges:
#     print(edge)
# 사이클 확인을 하기 위해서.. 각 정점을 이용해서 서로소 집합 만들기
def union(x, y):
    rx = find_set(x)
    ry = find_set(y)
    p[rx] = ry



def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])



p = [x for x in range(V)]


def kruskal():
    # 각 정점들이 cycle 이 생기지 않도록 간선 선택
    MST = []
    # 간선을 가중치 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    for i in range(E):
        # edges[i][0], edges[i][1] << 간선을 구성하는 정점
        # 똑같으면 같은 그룹에 있으니까...
        if find_set(edges[i][0]) != find_set(edges[i][1]):
            MST.append(edges[i])
            union(edges[i][0],edges[i][1])

    print(MST)
kruskal()

