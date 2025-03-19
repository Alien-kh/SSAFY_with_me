import sys

white_square = [[0] * 101 for _ in range(101)] # 백지장 제작, 101로 설정한 이유는 0인덱스 줄,칸은 안 쓸 예정이라서.
square_num = int(sys.stdin.readline()) # 사각형 갯수
cnt = 0 # 값 변수

for s_num in range(square_num): # 사각형 갯수만큼 반복
    x_start, y_start = map(int, sys.stdin.readline().split()) # X축, Y축 시작점 입력
    for i in range(y_start, y_start+10): # 사각형은 10칸씩 ( 세로 )
        for j in range(x_start, x_start+10): # 사각형은 10칸씩 ( 가로 )
            white_square[i][j] = 1 # 해당 칸은 1로 입력

for i in range(1, 101):
    for j in range(1, 101):
        if white_square[i][j] == 1: # 만약 해당 칸이 1이었다면,
            cnt += 1 # 색칠된 칸 수 1 추가

print(cnt)