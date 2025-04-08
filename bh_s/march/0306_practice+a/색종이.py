N = int(input())
paper = [[0] * 100 for _ in range(100)] # 종이는 100 x 100

for _ in range(N):
    x, y = map(int, input().split())    # 색종이의 너비(x), 높이(y)

    # 우리는 가로, 세로 길이가 각각 10이라는 것을 알고있으니, 색종이를 붙인 곳 기준으로 행/열 이동으로 봐도 된다.
    for i in range(y, y + 10): 
        for j in range(x, x + 10):
            paper[i][j] = 1


# 구하려는 곳은 색종이가 가린 부분임. 즉 색종이가 붙은 영역이 중첩되는 것을 다시 처리해야함.
area = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            area += 1

print(area)
