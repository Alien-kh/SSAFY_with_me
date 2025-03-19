from collections import deque


def dfs(start_dfs):
    dfs_result.append(start_dfs) # 현재 노드 리스트에 추가
    visited_dfs[start_dfs] = 1 # 방문한 노드의 visited 주소를 1로 변경
    for i in node_map_list[start_dfs]: # node_map_list에서 다음 노드로 갈 좌표를 찾기
        if visited_dfs[i] == 0: # 만약 해당 노드가 방문한 적 없는 노드라면
            dfs(i) # 재귀한다.


def bfs(start_bfs):
    bfs_deque = deque() # 빈 덱 생성
    bfs_deque.append(start_bfs) # 현재 위치를 덱에 추가
    visited_bfs[start_bfs] = 1 # 방문한 노드의 visited 주소를 1로 변경
    while bfs_deque: # 덱이 계속 존재하는 한 반복됨
        current = bfs_deque.popleft() # 현 위치를 popleft해서 받음
        bfs_result.append(current) # 그리고 현 노드를 리스트에 추가
        for i in node_map_list[current]: # node_map_list에서 다음 노드로 갈 좌표를 찾기
            if visited_bfs[i] == 0: # 만약 방문한 적 없는 노드라면
                visited_bfs[i] = 1 # 해당 노드를 방문처리하고
                bfs_deque.append(i) # deque에 append한다.


node_num, edge_num, start_node = map(int, input().split())

node_map_list = [[] for _ in range(node_num + 1)]  # 빈 리스트를 만든다. +1을 한 이유는 0번째 칸을 쓰지않음으로서 인덱스와 일치시키기 위함

for _ in range(edge_num):
    start, end = map(int, input().split())  # 시작지점 종료지점을 각각 입력
    node_map_list[start].append(end)
    node_map_list[end].append(start)  # 양방향 에지 설정

for i in range(node_num + 1):
    node_map_list[i].sort()  # 내림 차순으로 정렬

visited_dfs = [0] * (node_num + 1) # dfs의 방문 리스트를 만든다
dfs_result = [] # 출력 저장용으로 빈 리스트 제작
dfs(start_node) # def 호출

print(*dfs_result) # 형변환 한 후 출력

visited_bfs = [0] * (node_num + 1) # bfs의 방문 리스트를 만든다.
bfs_result = [] # 출력 저장용으로 빈 리스트를 제작
bfs(start_node) # def 호출

print(*bfs_result) # 형변환 후 출력
