def count_sub_node(node):
    if node ==None: # 노드가 없다면
        return 0
    left_count = count_sub_node(tree[node][0]) # 왼쪽
    right_count  = count_sub_node(tree[node][1]) # 오른쪽
    return 1 + left_count + right_count # 현재 노드 + 왼쪽 자식 + 오른쪽 자식

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split()) # 간선의 개수 E, N은 루트가 될 것
    V = E +1 # 노드 개수
    tree = [[None, None] for _ in range(V+1)]
    edges = list(map(int, input().split()))
    for i in range(0, 2*E, 2):
        if tree[edges[i]][0] is None: # 왼쪽 자식이 비었따면
            tree[edges[i]][0] = edges[i + 1]
        else:
            tree[edges[i]][1] = edges[i + 1]
    result = count_sub_node(N)
    print(f'#{tc} {result}')

'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''