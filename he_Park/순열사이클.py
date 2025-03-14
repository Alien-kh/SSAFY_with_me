T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    adj = [0] + list(map(int, input().split()))  # 인덱스 번호랑 노드 번호랑 맞춰줌
    visited = [0] * (N + 1)
    cnt = 0
    for i in range(1, N + 1):  # 1번부터 순회
        if not visited[i]:
            arr = []  # 순회할 때마다 arr는 갱신됨
            num = i
            while True:
                arr.append(adj[num])
                visited[num] = 1
                if adj[num] == i:  # 자기자신이 나오면 한 사이클이 종료된다
                    cnt += 1
                    break
                num = adj[num]
    print(cnt)