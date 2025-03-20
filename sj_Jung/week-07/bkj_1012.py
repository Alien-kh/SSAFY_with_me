import sys
sys.setrecursionlimit(10**6) # 재귀 허용 용량을 늘린다.

def delta_worm(start_x, start_y): # 지렁이가 투입될 장소 주변에 양배추가 추가로 더 있는지 확인하기 위한 def
    visited[start_y][start_x] = 1 # 일단 그 장소에 양배추가 심어져 있으니 방문했다 치고,

    delta_x = [1, -1, 0, 0]
    delta_y = [0, 0, 1, -1] # 델타 탐색을 위한 좌표 0 - 오른쪽, 1 - 왼쪽, 2 - 위쪽, 3 - 아래쪽

    for dir in range(4): # 네 방향 확인
        if start_x + delta_x[dir] >= 0 and start_x + delta_x[dir] < len_x and start_y + delta_y[dir] >= 0 and start_y + delta_y[dir] < len_y: # 리스트를 벗어나지 마렴.
            new_x = start_x + delta_x[dir] # 탐색할 x 좌표
            new_y = start_y + delta_y[dir] # 탐색할 y 좌표
            if cab_map[new_y][new_x] == 1 and visited[new_y][new_x] == 0: # 만약 해당 좌표에 양배추가 있고 방문한 적이 없다면,
                delta_worm(new_x, new_y) # 그 좌표를 중심점을 바꾸고 재귀한다.

testcase = int(sys.stdin.readline()) # 테스트 케이스 입력

for _ in range(1, testcase + 1): # 이 문제는 테스트 케이스를 따로 출력할 필요가 없으므로 _ 로 지정한다.
    len_x, len_y, cab_num = map(int, sys.stdin.readline().split()) # 배추밭의 가로갈이, 배추밭의 세로길이, 양배추 갯수
    cab_map = [[0] * len_x for _ in range(len_y)] # 양배추 지도
    visited = [[0] * len_x for _ in range(len_y)] # 방문 여부 지도

    for i in range(cab_num): # 양배추를 심어보자
        cab_x, cab_y = map(int, sys.stdin.readline().split()) # 양배추의 좌표를 입력
        cab_map[cab_y][cab_x] = 1 # 그 좌표에 양배추 심기(1 넣기)

    cnt = 0 # 필요한 지렁이의 갯수를 저장할 변수

    for y in range(len_y):
        for x in range(len_x):
            if visited[y][x] == 0 and cab_map[y][x] == 1: # 만약 방문한 적이 없고 양배추가 심어져 있다면
                delta_worm(x, y) # def 호출
                cnt += 1 # 지렁이 필요 갯수 1 추가

    print(cnt) # 결과 출력