'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''
def bfs(s, V):  # 시작 정점 s, 마지막 정점 V
    # visited 생성
    visited = [0] * (V + 1)     # visited 생성
    # 큐 생성
    q = [s]                     #시작점 enqueue
    # q. append(s)                #시작점 enqueue
    visited[s] = 1              # 시작점 enqueue 표시(visited) ---> 여기까지가 초기화 과정
    while q:                    # 큐가 비워질 때 까지 반복, front != rear
        t = q.pop(0)            # dequeue해서 t에 저장 / 만약에 pop()을 그냥 해버리면 (0을 안 넣어주고) 일종의 dfs가 되버림
        print(t)                # t정점에 대한 처리
        for w in adj_l[t]:      # t에 인접한 정점 w 중, 인큐되지 않은 정점이 있으면
            if visited[w] == 0:
                q.append(w)     # enqueue, enqueue 표시
                visited[w] = visited[t] + 1
    print(visited)


V, E = map(int,input().split())   # 1번 부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))

# 인접 리스트 ---------------
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2 +1]
    adj_l[v1].append((v2))
    adj_l[v2].append((v1))  # 방향이 없는 경우

bfs(5, 7)