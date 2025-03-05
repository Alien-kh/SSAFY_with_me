T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())  # N: 전체 노드 개수, M: 리프 노드 개수, L: 출력할 노드 번호
    tree = [0] * (N + 1)  # 1번부터 시작하는 완전 이진 트리

    for _ in range(M):
        node_num, value = map(int, input().split())
        tree[node_num] = value  # 리프 노드 값 저장

    # 부모 노드의 값 계산 (자식 노드들의 합)
    for i in range(N, 0, -1):  # 마지막 노드부터 1번 노드까지 거꾸로 계산
        parent = i // 2
        if parent > 0:
            tree[parent] += tree[i]

    print(f"#{tc} {tree[L]}")
