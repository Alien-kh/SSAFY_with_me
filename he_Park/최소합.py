def solve(r, c, sum_v):
    global min_v
    if min_v <= sum_v:  # 가지치기
        return
    if r == c == N - 1:
        if min_v > sum_v:
            min_v = sum_v
        return

    if r + 1 < N:
        solve(r + 1, c, sum_v + arr[r + 1][c])  # 오른쪽으로 이동
    if c + 1 < N:
        solve(r, c + 1, sum_v + arr[r][c + 1])  # 오른쪽으로 이동
    
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 99999
    solve(0, 0, arr[0][0])
    print(f'#{tc} {min_v}')