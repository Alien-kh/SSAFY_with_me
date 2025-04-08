# 지나가는 루트의 최소합을 구하는 함수
def min_root(x, y, sum):
    global min_sum
    if x >= N or y >= N:    # 경로를 벗어난 경우 return
        return
    if  x == N-1 and y == N-1:  # 도착지점에 도달한 경우 return
        if sum + arr[x][y] < min_sum:       # 최소합인지 확인
            min_sum = sum + arr[x][y]
        return

    min_root(x, y+1, sum+arr[x][y])
    min_root(x+1, y, sum+arr[x][y])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 0xffffffff
    min_root(0,0,0)
    print(f'#{tc} {min_sum}')