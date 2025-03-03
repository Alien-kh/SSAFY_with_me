N = int(input()) #컴퓨터의 개수
M = int(input()) # 간선의 개수
# 인접 리스트 만들어주기
adj_v = [[] for _ in range(N+1)] # 0부터  N번까지
for _ in range(M):
    v1, v2 = map(int,input().split())
    adj_v[v1].append(v2)# 서로 연결되어 있음
    adj_v[v2].append(v1)
count = 0 # 감염된 컴퓨터
def bfs(start):
    global count
    visited = [0] * (N+1) # 방문 리스트
    q = [start] # 시작점 넣어주기
    visited[start] = 1 # 시작점 방문 표시
    while q: # q가 비어있지 않다면
        a = q.pop(0)# 맨 앞 컴퓨터 번호 뺴서
        for w in adj_v[a]: # 연결된 정점들 찾아서 방문했는지 확인
            if visited[w] == 0: # 방문하지 않았따면
                q.append(w) # q에 넣어주고
                visited[w] = 1 # 방문 처리
                count +=1
    return count

print(bfs(1))