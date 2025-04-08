from collections import deque

def bfs(N, K):
    if N >= K:
        return N - K  # 뒤로 걷기만 하는 경우

    # 방문 배열 (각 위치까지 걸린 최소 시간 저장)
    visited = [-1] * 100001  
    queue = deque([N])
    visited[N] = 0  # 시작 위치

    while queue:
        pos = queue.popleft()  # 현재 위치
        
        # 동생을 찾으면 종료
        if pos == K:
            return visited[pos]

        # 이동 가능한 경우 탐색 (순간이동 먼저)
        for next_pos in [pos * 2, pos - 1, pos + 1]:
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1:  # 방문한 적 없는 곳만
                if next_pos == pos * 2:  # 순간이동 (비용 0)
                    visited[next_pos] = visited[pos]
                    queue.appendleft(next_pos)  # 0초 이동이므로 우선 탐색
                else:  # 걷기 (비용 1)
                    visited[next_pos] = visited[pos] + 1
                    queue.append(next_pos)

# 입력 예시
N, K = map(int, input().split())
print(bfs(N, K))
