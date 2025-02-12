T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    result = 0
    for i in range(N):
        for j in range(M):
            total = arr[i][j]
            cnt = arr[i][j]
            for k in range(4):
                    for l in range(1,cnt+1):
                        a = i + dx[k] * l
                        b = j + dy[k] * l
                        
                        if -1 < a < N and -1 < b < M:
                            total += arr[a][b]

            if total > result:
                result = total

    print(f'#{test_case} {result}')
