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
# 시작점을 알 수 없으니.... 모든 점에서 다 시작해보기
# 사방탐색 델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
max_length = 0  # 제일 긴 길이
for i in range(N):
    for j in range(N):
        r, c = i, j
        length = 1
        while True:
            # i,j 시작점
            # 사방탐색해서 제일 작은 위치 찾기
            min_nr, min_nc = -1, -1  # 위쪽 방향을 초기값으로 설정
            min_v = 0xfffffff
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < N:  # 정상범위
                    if arr[nr][nc] < arr[r][c] and arr[nr][nc] < min_v:
                        min_v = arr[nr][nc]
                        min_nr = nr
                        min_nc = nc
            # 최저점 찾음
            if (min_nr, min_nc) != (-1,-1): #작은 값이 없는 경우가 아니라면,
                r,c = min_nr,min_nc
                length += 1
            else:
                break   #나보다 낮은거 못찾음
        if max_length < length:
            max_length = length
print(max_length)



