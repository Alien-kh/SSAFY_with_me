def solve():
    global min_v
    cnt1 = cnt2 = 0
    for i in range(N):
        for j in range(i + 1, N):
            if not visited[i] and not visited[j]:
                cnt1 += (arr[i][j] + arr[j][i])
            elif visited[i] and visited[j]:
                cnt2 += (arr[i][j] + arr[j][i])

    if min_v > abs(cnt1 - cnt2):
        min_v = abs(cnt1 - cnt2)
    return


def recur(cnt, start):
    if cnt == N//2:
        solve()
        return

    for i in range(start, len(li)):
        visited[i] = 1
        recur(cnt + 1, i + 1)
        visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = [i for i in range(N)]

    visited = [0] * N
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = float('inf')

    recur(0, 0)

    print(f'#{tc} {min_v}')
