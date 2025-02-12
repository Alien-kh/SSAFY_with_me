T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    r, c = 0, 0

    arr = [[0 for _ in range(N)] for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    num = 1
    while True:
        arr[r][c] = num
        num += 1
        r = r + dr[d]
        c = c + dc[d]
        if num == N * N + 1:
            break
        if c >= N or r >= N or c < 0 or r < 0 or arr[r][c]:
            r -= dr[d]
            c -= dc[d]
            d = (d + 1) % 4
            r += dr[d]
            c += dc[d]
    print(f'#{test_case}')
    for row in range(len(arr)):
        for col in range(len(arr)):
            print(arr[row][col],end = " ")
        print()