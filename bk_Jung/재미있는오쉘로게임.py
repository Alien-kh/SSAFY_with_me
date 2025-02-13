T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]    
    if N == 4:
        arr[1][1] = 2
        arr[1][2] = 1
        arr[2][1] = 1
        arr[2][2] = 2
    elif N == 6:
        arr[2][2] = 2
        arr[2][3] = 1
        arr[3][2] = 1
        arr[3][3] = 2
    elif N == 8:
        arr[3][3] = 2
        arr[3][4] = 1
        arr[4][3] = 1
        arr[4][4] = 2
 
    cnt_black = 0
    cnt_white = 0
 
    dx = [-1,1,0,0,1,1,-1,-1]
    dy = [0,0,-1,1,1,-1,1,-1]
 
    for i in range(M):
        x,y,color = map(int,input().split())
        x -= 1
        y -= 1
         
        arr[x][y] = color # 돌 두기
        for k in range(8):  # 방향 탐색
                a = x + dx[k]
                b = y + dy[k]
                rev = []
                while -1 < a < N and -1 < b < N:
                    if arr[a][b] == 0:
                        break
                    if arr[a][b] == color:
                        for ax,ay in rev:
                            arr[ax][ay] = color
                        break
                    rev.append((a,b))    
                    a += dx[k]
                    b += dy[k]             
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt_black +=1
            elif arr[i][j] == 2:
                cnt_white +=1
 
 
    print(f'#{test_case} {cnt_black} {cnt_white}')