T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N: 퍼즐 크기, K: 단어 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    # 가로 방향
    for i in range(N):  # 각 행에 대해
        for j in range(N - K + 1):  # K칸 단어가 들어갈 수 있는 시작위치
            is_valid = True  # 현재 구간이 연속된 1로 이루어졌는지 확인

            for k in range(K):  # K칸 동안 1인지 확인
                if puzzle[i][j + k] != 1:
                    is_valid = False
                    break

            if is_valid:
                left = j - 1
                right = j + K

                # 왼쪽이 범위 밖이거나 0이고, 오른쪽도 범위 밖이거나 0이면
                if (left < 0 or puzzle[i][left] == 0) and (right >= N or puzzle[i][right] == 0):
                    cnt += 1

    # 세로 방향
    for j in range(N):  # 각 열에 대해
        for i in range(N - K + 1):  # K칸 단어가 들어갈 수 있는 시작 위치들
            is_valid = True

            for k in range(K):  # 세로로 K칸 동안 1인지 확인
                if puzzle[i + k][j] != 1:
                    is_valid = False
                    break

            if is_valid:
                top = i - 1
                bottom = i + K

                # 위쪽이 범위 밖이거나 0이고, 아래도 범위 밖이거나 0이면
                if (top < 0 or puzzle[top][j] == 0) and (bottom >= N or puzzle[bottom][j] == 0):
                    cnt += 1

    print(f'#{tc} {cnt}')
