def solve():
    for row in range(0, 7, 3): # 0부터 6까지 3*3으로 확인
        for col in range(0, 7, 3):
            sudoku = [] # 1~9검증을 위해 set설정
            for i in range(3):
                for j in range(3): # 3 *3 sudoku확인을 위해
                    sudoku.append(arr[row+i][col+j])
            if len(set(sudoku)) != 9: # 9개 숫자가 없다면 false
                return 0
    # 여기까지 오면 3*3 은 통과
    for r in range(9):
        arr_r = arr[r]
        if len(set(arr_r)) != 9: # 열도 확인
            return 0
    c_arr = list(map(list,zip(*arr))) # 리스트 집하는 법 다시 잘 알아두자 (대각선 뒤집기? 아무튼 [col][row]해주는거)
    for c in range(9):
        arr_c = c_arr[c]
        if len(set(arr_c)) != 9:
            return 0
    # 행열까지 다 통과했으면 ok
    return 1




T = int(input()) # 테스트 케이스
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)] # 9 * 9
    result = solve()
    print(f'#{tc} {result}')