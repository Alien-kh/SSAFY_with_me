# 전위 순회: 루트노드에서 작업 처리하고, 왼쪽 서브트리, 오른쪽 서브트리
def preorder(v):
    if v  is None: # 해당 번호 노드가 없으면...
        return
    # v번 노드에서 작업 처리 하기
    # 왼쪽 자식: (v * 2)번
    # 오른쪽 자식: (V * 2) + 1 번
    preorder(left[v])
    print(tree[v],end ="")
    preorder(right[v])


T = 10
for tc in range(1,T+1):
    N = int(input())
    left = [None] * (N+1)
    right = [None] * (N+1)
    tree = [None] * (N+1)
    for i in range(N):
        arr = input().split()
        a = int(arr[0])
        b = arr[1]
        tree[a] = b
        if len(arr) > 2:
            c = int(arr[2])
            left[a] = c
        if len(arr) > 3:
            d = int(arr[3])
            right[a] = d

    print(f'#{tc}',end = " ")
    preorder(1)
    print()
