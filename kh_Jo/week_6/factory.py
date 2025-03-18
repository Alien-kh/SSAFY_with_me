def check(row,col):
    for i in range(row):
        if visited[i][col]:
            return False
    return True

def solve(row, v):
    global min_v
    if v >= min_v: # 이미 최솟값보다 크다면 Return
        return

    if row == N:# 끝까지 도착했을 때 확인
        if min_v >= v:
            min_v = v
        return
    for col in range(N):
        if check(row, col) is False: # 이전에 방문한 열인지 확인
            continue
        visited[row][col] = 1
        next_v = v + arr[row][col]
        solve(row+1, next_v)
        visited[row][col] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    min_v = 21e8 # 최솟값
    for _ in range(N):
        arr.append(list(map(int,input().split())))# 배열 만들어주기
    visited = [[0] * N for _ in range(N)]
    solve(0,0)
    print(f'#{tc} {min_v}')