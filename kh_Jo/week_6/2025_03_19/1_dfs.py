import sys
sys.stdin = open('graph.txt', 'r')

def dfs(node):
    # 재귀 dfs의 경우, 재귀임에도 종료조건이 없음 => 방문 처리 방식으로 언젠가 끝이 나기에 종료조건이 없는 경우가 많음

    # 그래서 보통 그래프 문제들에서 이 부분에 가지치기가 들어감 ex) K개의 노드 방문했다면 종료
    # ex) N 개를 모두 방문했다면 경로 출력
    # if 종료시 해야할 것들 or 가지치기: return
    print(node, end=' ')
    # visited[node] = 1 # 문제마다, 개발자마다 구현 방식이 다르다 초기화하는 구간

    # 현재 노드에서 인접한 노드들을 모두 확인하면서, 한 군데로 진행
    for next_node in graph[node]:
        if visited[next_node]:
            continue
        visited[next_node] = 1
        dfs(next_node)





N, M = map(int, input().split())
# 1. 그래프를 저장하기
# - 비어있는 그래프를 생성한다.
# - 그래프 정보를 입력받아 넣는다.
# graph = [[0] * (N) for _ in range(N+1)]# 인접 행렬 ( N * N 의  0 배열)
# 인접 리스트 (N * N ([]))
graph = [[] for _ in range(N+1)] # 입접 리스트(N * N ([])
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s) # 양 방향이라면, 뒤집어서 저장도 해주어야 한다.

visited = [0] * (N+1) # 방문 여부 기록
visited[1] = 1 # 출발점 초기화
dfs(1)

# for row in graph:
#     print(*row)