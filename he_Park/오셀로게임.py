# 실패
def func():
    for d in [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]:
        dr = r + d[0]
        dc = c + d[1]
        cnt = 0
        is_find = False
        while 0 < dr <= N and 0 < dc <= N:
            if arr[dr][dc] == 3 - colour:  # 내 옆에 상대편의 돌이 있다면
                is_find = True
                dr += d[0]
                dc += d[1]
                cnt += 1
                continue
            elif is_find and arr[dr][dc] == colour:  # 내 돌을 발견하면 조건을 만족하므로
                arr[r][c] = colour  # 돌을 놓는다. 그리고
                for i in range(1, cnt + 1):
                    arr[r + d[0] * i][c + d[1] * i] = colour  # 상대편의 돌을 내 돌로 만든다.
                return  # 다음 턴으로 넘어간다.
            else:  # 내 옆에 상대편의 돌이 없는 경우
                break


T = int(input().strip())
for tc in range(1, T+1):
    N, M = map(int, input().strip().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    # 초기 설정
    arr[N // 2][N // 2] = arr[N // 2 + 1][N // 2 + 1] = 2  # 2: 백돌
    arr[N // 2 + 1][N // 2] = arr[N // 2][N // 2 + 1] = 1  # 1: 흑돌
    for _ in range(M):
        c, r, colour = map(int, input().strip().split())  # 1 2 1
        func()

    # print(arr)
    arr1 = []
    for i in arr:
        arr1.extend(i)
    print(arr1)
    # print(f'#{tc} {arr1.count(1)} {arr1.count(2)}')