def delta_move(start_x, start_y):
    global cango
    if start_x == horizen - 1 and start_y == vertical - 1: # 만약 가장 오른쪽 아래에 도달했다면
        cango = 'Yes' # 판정을 Yes로 설정하고 return
        return

    delta_y = [0, 1]
    delta_x = [1, 0] # 델타 리스트 정의

    for dir in range(2):
        if start_x + delta_x[dir] >= 0 and start_x + delta_x[dir] < horizen and start_y + delta_y[dir] >= 0 and start_y + delta_y[dir] < vertical: # 지도를 벗어나지 말것
            new_y = start_y + delta_y[dir]
            new_x = start_x + delta_x[dir]  # 탐색할 x 좌표 # 탐색할 y 좌표
            if visited[new_y][new_x] == 0 and roadtobitcoin[new_y][new_x] == 1 and cango == 'No': # 방문한 적 없고, 갈 수 있는 곳이며, 이미 목적지에 도달한 상태가 아니라면
                visited[new_y][new_x] = 1 # 그 쪽은 방문다고 하고
                delta_move(new_x, new_y) # 재귀하여 기준점을 변경


horizen, vertical = map(int, input().split()) # 가로와 세로
roadtobitcoin = [list(map(int, input().split())) for _ in range(vertical)] # 지도 입력 받기
visited = [[0] * horizen for _ in range(vertical)] # 방문 지도 정의

cango = 'No' # 최종 목표에 도달했는지를 나타내는 str

visited[0][0] = 1 # 0,0 에서 시작하므로 방문했다고 사전 지정
delta_move(0, 0) # 0,0 부터 시작

print(cango) # 답을 출력
