T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
 
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
 
    dx = [-1,1,0,0,1,1,-1,-1]
    dy = [0,0,-1,1,1,-1,1,-1]
    result = 0
    for i in range(N):
        for j in range(M):
            h = arr[i][j]
            cnt = 0
            for k in range(8):
                a = i + dx[k]
                b = j + dy[k]
 
                if -1 < a < N and -1 < b < M:
                    if arr[a][b] < h:
                         cnt +=1
            if cnt >= 4:
                result += 1
 
    print(f'#{test_case} {result}')