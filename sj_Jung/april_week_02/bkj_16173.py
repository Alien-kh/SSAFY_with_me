def checker(start_x, start_y):
    global answer
    if start_x >= map_len or start_y >= map_len: # 지도 공간을 벗어난다면, 바로 리턴한다.
        return

    if game_map[start_y][start_x] == 0: # 만약 현 위치의 값이 0이라면 무한루프에 빠지므로 즉시 리턴
        return

    if game_map[start_y][start_x] == -1: # 최종 목표에 도달할 시
        answer = 'HaruHaru' # 출력할 문구를 HaruHaru로 변경
        return

    dy = [0, 1]
    dx = [1, 0] # 델타 탐색용 리스트

    for dir in range(2):
        new_x = game_map[start_y][start_x] * dx[dir] + start_x
        new_y = game_map[start_y][start_x] * dy[dir] + start_y # 젤리가 움직일 수 있는 곳은 현재 위치의 칸의 값 "만큼"
        if answer == 'HaruHaru': # 만약 목표장소에 도달했다면 즉시 리턴.
            return
        else: # 그게 아니라면
            checker(new_x, new_y) # 기준점을 이동 지점으로 바꾼 뒤 재귀

map_len = int(input()) # 맵 크기

game_map = [list(map(int, input().split())) for _ in range(map_len)] # 지도 제작

answer = 'Hing' # 기본 값을 'Hing'으로 지점

checker(0, 0) # check def 호출

print(answer) # 답 출력