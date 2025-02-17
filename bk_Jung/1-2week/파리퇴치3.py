T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    total = 0
    result = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    di = [1,-1,-1,1]
    dj = [1,1,-1,-1]

    for i in range(N):
        for j in range(N):
            cnt1 = arr[i][j]
            cnt2 = arr[i][j]

            for k in range(4):
                for l in range(1,M):
                    a = i + dx[k] * l
                    b = j + dy[k] * l

                    c = i + di[k] * l
                    d = j + dj[k] * l
                    if -1 < a < N and -1 < b < N:
                        cnt1 += arr[a][b]
                    if -1 < c < N and -1 < d < N:
                        cnt2 += arr[c][d]
            total = max(cnt1,cnt2)
            if result < total:
                result = total


    print(f'#{test_case} {result}')        

