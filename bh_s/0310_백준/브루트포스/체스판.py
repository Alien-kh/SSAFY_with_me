# N, M 입력 받기
N, M = map(int, input().split())

# 보드 상태 입력 받기
board = [input().strip() for _ in range(N)]


# 체스판이 두 가지 경우로 나뉘므로, 두 가지 색을 기준으로 비교
def count_changes(x, y, board, start_color):
    changes = 0
    # start_color: 0 -> W, 1 -> B
    for i in range(8):
        for j in range(8):
            expected_color = (start_color + i + j) % 2  # (0 or 1)
            actual_color = 0 if board[x + i][y + j] == 'W' else 1
            if expected_color != actual_color:
                changes += 1
    return changes


# 최소 칠해야 하는 칸을 찾기 위한 변수
min_changes = float('inf')

# 8x8 크기의 모든 부분 보드에 대해 탐색
for i in range(N - 7):
    for j in range(M - 7):
        # 1. 왼쪽 위가 흰색인 경우 (start_color = 0)
        changes_start_white = count_changes(i, j, board, 0)
        # 2. 왼쪽 위가 검은색인 경우 (start_color = 1)
        changes_start_black = count_changes(i, j, board, 1)

        # 두 경우의 최소값을 취함
        min_changes = min(min_changes, changes_start_white, changes_start_black)

# 결과 출력
print(min_changes)