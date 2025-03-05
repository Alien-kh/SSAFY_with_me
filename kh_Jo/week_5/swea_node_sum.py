T = int(input())
for tc in range(1, T+1):
    N,M,L = map(int, input().split())   # N은 노드의 개수 M은 간선의 개수, 값을 출력한 노드 번호 L
    tree = [None] * (N+1) # N 번 idx까지 사용해야 하니깐
    for _ in range(M):
        node_idx, num = map(int,input().split())
        tree[node_idx] = num
    for i in range(N, 1, -1): #맨 끝 노드부터
        if i % 2 != 0: # 홀 수 일떄
            tree[i//2] = tree[i] + tree[i-1]
        else:
            if i+1 <= N and tree[i+1]:# 오른쪽 노드가 있따면
                tree[i//2] = tree[i] + tree[i+1]
            else:
                tree[i//2] = tree[i]

    print(f'#{tc} {tree[L]}')