from collections import deque

def solve():
    q = deque()
    min_cnt = 21e8
    q.append((K, 0))
    visited = [0] * 1000001    
    while q:
        curr, cnt= q.popleft()
        if visited[curr] == 1:
            continue # 만약에 나온 적이 있는 값이면 볼 필요 X
        visited[curr] = 1
        if curr < 0:
            continue
        if cnt >= min_cnt:
            continue # cnt보다 크면 의미 X
        if curr == N:
            if min_cnt > cnt:
                min_cnt = cnt
            return min_cnt
        if curr % 2 ==0:
            q.append((curr//2, cnt+1))  # 짝수일 때만 나눠줌으로 가지치기
        q.append((curr-1, cnt+1))
        q.append((curr+1, cnt+1)) 
    return min_cnt

N, K = map(int, input().split())# N이 수빈이 위치 , K는 동생위치

print(solve())
