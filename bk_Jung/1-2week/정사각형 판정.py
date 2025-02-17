
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    arr = [list(input()) for _ in range(N)]
    b = sum(row.count('#') for row in arr) # 전체 # 갯수
    x = 0
    y = 0

    find_start = False
    for i in range(N): # 시작위치 찾기
        for j in range(N):
            if arr[i][j] == '#':
                x = i
                y = j
                find_start = True
                break
        if find_start:
            break

    row_cnt = 0
    for i in range(y,N): # 가로 크기
        if arr[x][i] == '#':
            row_cnt +=1
        else:
            break

    col_cnt = 0
    for i in range(x,N): # 세로 크기
        if arr[i][y] == '#':
            col_cnt +=1
        else:
            break

    if row_cnt != col_cnt:
        print(f'#{test_case} no')

    cnt = 0
    stop = False
    for i in range(x,x+row_cnt):
        for j in range(y,y+col_cnt):
            if arr[i][j] != '#':
                print(f'#{test_case} no')
                stop = True
                break
            else:
                cnt += 1
        if stop:
            break
    else:
        if cnt == b:
            print(f'#{test_case} yes')
        else:
            print(f'#{test_case} no')
