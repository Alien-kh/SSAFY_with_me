# gpt의 도움을 받음. 다시 풀어보기
# 도화지: 100 x 100
# 색종이: 10 x 10
# 색종이가 붙은 검은 영역의 넓이
blank = [[0] * 101 for _ in range(101)]  # 도화지
T = int(input())
for _ in range(T):
    r, c = map(int, input().split())  # 색종이 왼쪽 아래 꼭짓점 좌표
    # 색종이 붙이기 (10x10 크기)
    for i in range(10):
        for j in range(10):
            blank[c + i][r + j] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if blank[i][j] == 1:
            cnt += 1
print(cnt)