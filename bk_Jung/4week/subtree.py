def preorder(v):
    global cnt
    if v is None or v >= len(tree):  # 존재하지 않는 노드 체크
        return
    cnt += 1  # 현재 노드 방문 처리
    if tree[v][0] is not None:  # 왼쪽 자식 방문
        preorder(tree[v][0])
    if tree[v][1] is not None:  # 오른쪽 자식 방문
        preorder(tree[v][1])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    tree = [[None, None] for _ in range(E + 2)]  # 트리 초기화
    edges = list(map(int, input().split()))

    for i in range(0, len(edges), 2):
        parent, child = edges[i], edges[i + 1]
        if tree[parent][0] is None:
            tree[parent][0] = child
        else:
            tree[parent][1] = child

    cnt = 0  # 노드 개수 카운트
    preorder(N)  # N번 노드를 루트로 서브트리 탐색
    print(f"#{tc} {cnt}")  # 결과 출력
