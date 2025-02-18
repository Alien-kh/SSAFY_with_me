def move(r, c):
    global max_cnt
    global cnt
    global current
    for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        dr = r + d[0]
        dc = c + d[1]
        if 0 <= dr < N and 0 <= dc < N:
            if current > arr[dr][dc]:
                current = arr[dr][dc]  # 현재 위치 갱신
                nr, nc = dr, dc  # nr, nc: 새로운 현재 위치
    if current == arr[r][c]:  # 현재 값이 최소면(더이상 갱신이 안되면)
        if max_cnt < cnt:
            max_cnt = cnt
        return
    else:  # 갱신이 되면
        cnt += 1
        move(nr, nc)



T = int(input().strip())
for tc in range(1, T+1):
    N = int(input().strip())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    max_cnt = 0  # 최대 이동 거리의 최댓값
    for r in range(N):
        for c in range(N):
            cnt = 1  # 현재위치 (r,c)에서의 이동 거리
            current = arr[r][c]
            move(r, c)

    print(f'#{tc} {max_cnt}')