# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]

arr = [
    [9, 6, 7, 15, 8],
    [14, 1, 2, 3, 11],
    [25, 5, 10, 12, 19],
    [13, 18, 4, 16, 21],
    [24, 22, 23, 3, 20],
]
N = 5
dr = [-1, 1, 0, 0] # 상하 좌우
dc = [0, 0, -1, 1]
count = 1
min_val = 21e8
max_count = 0
for i in range(N):
    for j in range(N):
        count = 1
        min_val = arr[i][j] # 현재위치에서 점점 작은 점으로 이동해야하니깐
        r, c = i, j # 시작 지점
        while True: # 계속 이동 해야 하므로
            ar, ac = 'a', 'a'
            for d in range(4):# 4방향 이동
                nr = r + dr[d]
                nc = c + dc[d]
                if 0<= nr < N and 0<= nc < N:
                    if arr[nr][nc] < min_val: # 만약 다음 이동하는 값이 작다면
                        min_val = arr[nr][nc]
                        ar, ac = nr, nc
            # 4방향 측정이 끝난 후:
            if ar != 'a' and ac != 'a':
                count += 1 # 한 번 이동
                r,  c = ar, ac # 다음 칸으로 좌표 이동
            else: # 이동할 수 없을 때
                break
        if max_count < count:
            max_count = count
print(max_count)