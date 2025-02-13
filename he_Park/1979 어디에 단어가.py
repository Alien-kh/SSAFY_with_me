T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    I_found_it = 0  # 길이 K짜리 빈칸 개수 카운트
    for i in range(N):  # 행 우선 순회
        cnt = 0  # 연속된 1(흰 칸)의 개수 카운트
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if j == N-1:
                    if cnt == K:
                        I_found_it += 1
            else:
                if cnt == K:
                    I_found_it += 1
                cnt = 0

    for i in range(N):  # 열 우선 순회
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
                if j == N-1:
                    if cnt == K:
                        I_found_it += 1
            else:
                if cnt == K:
                    I_found_it += 1
                cnt = 0
    print(f'#{tc} {I_found_it}')