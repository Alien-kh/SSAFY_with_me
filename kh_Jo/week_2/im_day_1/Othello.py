def solve(row, col, color, arr, N):
    # 가로 세로 왼쪽 대각선 오른쪽 대각선
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    row -= 1 # 인덱스를 편하게 계산해주기 위해 1씩 다 빼줌
    col -= 1
    if arr[row][col] == 0: # 만약에 돌을 놓을 자리가 비어있다면(0)이라면
        # 대각선 방향에 상대 돌이 있는지 확인
        arr[row][col] = color #  돌을 항상 놓을 수 있음
        for d in range(8): # 8 방향 탐색
            can_flip =[]    # 뒤집을 수 있는 돌들을 일단 찾기 위한 리스트
            nr = row + dr[d]
            nc = col + dc[d]
            # 상대 돌이 돌이 있으면서 리스트 안에 있는 범위에서 계속 찾기
            while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 0 and arr[nr][nc] != color:
                can_flip.append((nr, nc))
                nr += dr[d]
                nc += dc[d]
                # 다 찾은 후에, 같은 색 돌이 있으면 뒤집어 주기
            if 0<= nr < N and 0 <= nc < N and arr[nr][nc] == color:
                for flip_row,flip_col in can_flip:
                    arr[flip_row][flip_col] =color
            #     arr[row][col] = color
            # else:
            #     continue # 만약에 조건에 부합하지 않다면 /놓을 수가 없다면 다음 턴으로 넘기기

def count_stones(arr):
    count_dict = {1: 0, 2: 0} # 1 흑 2 백

    for board_r in arr:
        for cell in board_r:
            if cell in count_dict:
                count_dict[cell] += 1
    return count_dict
        # 각각의 개수를 세준 뒤 딕셔너리에 갱신시켜서 반환
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # 여기서 N 은 돌판 M은 돌을 놓는 횟수
    arr = [[0]*N for _ in range(N)]
    # 흰 색은 2 검정색은 1 # 판의 idx는 0부터 시작하기에 1씩 더 뺴줌
    arr[N // 2 - 1][N // 2 - 1] = 2  # 백
    arr[N // 2 - 1][N // 2] = 1  # 흑
    arr[N // 2][N // 2 - 1] = 1  # 흑
    arr[N // 2][N // 2] = 2  # 백
    for i in range(M):
        row, col, color = map(int, input().split())
        solve(row, col, color, arr, N)
    result = count_stones(arr)
    print(f'#{tc} {result[1]} {result[2]}')