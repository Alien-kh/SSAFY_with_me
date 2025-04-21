# from collections import deque
# deque쓰는 것보다 그냥 list queue를 쓰는게 더 빠르게 나온다.


def find_target(curr_size, curr):
    visited = [[False]* N for _ in range(N)]
    visited[curr[0]][curr[1]] = True
    dr = [-1, 0, 1, 0] # 상 좌 하 우
    dc = [0, -1, 0, 1]
    min_dist = 21e8
    # q = deque([(0, curr[0], curr[1])])
    q = [(0, curr[0], curr[1])]
    targets = [] # 만약 같은 거리에 있는 것이라면 r 기준으로 위쪽, c 기준으로 왼쪽에 있어야 하므로 일단 타겟에 넣어준뒤
    while q:
        dist , curr_r, curr_c = q.pop(0)
        if 0 < arr[curr_r][curr_c] < curr_size:
            if dist <= min_dist:
                min_dist = dist
                targets.append((dist, curr_r, curr_c))
            continue
        for d in range(4):
            nr, nc = curr_r + dr[d], curr_c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == False:
                if 0 <= arr[nr][nc] <= curr_size:
                    visited[nr][nc] = True
                    q.append((dist+1, nr, nc))

    if targets:
        targets.sort() # 거리를 기준으로 정렬시키고 -> r 기준 정렬 -> c 기준 정렬
        return targets[0]
    else:
        return None




def solve():

    for r in range(N):
        for c in range(N):
            if arr[r][c]==9:
                curr_r, curr_c = r,c
                arr[r][c] = 0
    curr_size = 2
    eaten = 0
    total_cnt = 0
    while True:
        result = find_target(curr_size,(curr_r, curr_c))
        if result is None: # 만약 물고기 못먹으면 바로 맘스터콜
            break
        dist, tar_r, tar_c  = result
        total_cnt += dist
        curr_r, curr_c = tar_r, tar_c
        arr[curr_r][curr_c] = 0
        eaten +=1
        if eaten == curr_size:
            curr_size +=1
            eaten = 0

    return total_cnt


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

result = solve()
print(result)

