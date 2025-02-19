T = int(input())
for tc in range(1, T+1):
    N, M =map(int, input().split())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    max_cnt = 0
    for i in range(N):  # 행 우선 순회
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
            else:
                cnt = 0
    for i in range(M):  # 열 우선 순회
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
            else:
                cnt = 0

    print(f'#{tc} {max_cnt}')