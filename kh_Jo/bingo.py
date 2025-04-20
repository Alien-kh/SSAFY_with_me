# 5*5 빙고 3빙고가되려면 몇번째 숫자에서?!

bingo = [list(map(int, input().split())) for _ in range(5)]
bunho = [list(map(int, input().split())) for _ in range(5)]
check = [[0] * 5 for _ in range(5)]
cnt = 0

def bingo_check(board):
    bingo_count = 0
    # 가로빙고 확인
    for row in board:
        if sum(row) == 5:
            bingo_count += 1
    # 세로빙고 확인
    for col in range(5):
        if sum(board[row][col] for row in range(5)) == 5:
            bingo_count += 1

    # 대각선빙고 확인
    if sum(board[i][i] for i in range(5)) == 5:
        bingo_count += 1

    if sum(board[i][4-i] for i in range(5)) == 5:
        bingo_count +=1
    return bingo_count


for i in range(5):
    for j in range(5):
        cnt += 1
        for k in range(5):
            for l in range(5):
                if bunho[i][j] == bingo[k][l]:
                    check[k][l] = 1

        # check 배열을 돌면서 빙고 됐는지 확인해야함,,
        # if cnt >= 12:
        if bingo_check(check) >=3:
            print(cnt)
            exit()
'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''