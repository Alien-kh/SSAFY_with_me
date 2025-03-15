cnt = 0

def preorder(v):
    global cnt
    if v is None:
        return
    cnt += 1
    preorder(left[v])
    preorder(right[v])

    return cnt



T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())  # E = 간선 갯수, N = 서브트리의 루트
    node = list(map(int, input().split()))
    left = [None] * (max(node) + 1)
    right = [None] * (max(node) + 1)

    for i in range((len(node) // 2)):
        node_num = node[2 * i]
        if left[node_num] is None:
            left[node_num] = node[2 * i + 1]
        else:
            right[node_num] = node[2 * i + 1]

    result = preorder(N)
    print(f'#{tc} {result}')
    cnt = 0