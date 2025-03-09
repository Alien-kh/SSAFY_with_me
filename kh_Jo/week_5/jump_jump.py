from collections import deque


def dfs(start):
    s = deque()
    s.append(start)
    direction = -1, 1 # 왼쪽 or 오른쪽으로만 이동 가능
    visited = [0] * (N)
    visited[start] = 1

    count = 1
    while s:# 스택이 남아있는 동안
        curr = s.pop()
        avi_move = arr[curr] # 이동 가능한 거리
        for d in direction:
            nr = curr + d  * avi_move# (왼쪽, 오른쪽 다 확인)
            if 0 <= nr < N and not visited[nr]: # 범위 이내이고, 이동할 수 있으며, 방문하지 않았다면 ㄱㄱ
                s.append(nr)
                visited[nr] = 1 # 방문처리
                count +=1


    return count


N = int(input()) # 돌의 개수
arr = list(map(int,input().split()))
start = int(input()) - 1 # idx로 바꿔주기
print(dfs(start))


