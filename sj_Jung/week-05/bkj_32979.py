from collections import deque

player = int(input())  # 플레이어 수
apartment_game = int(input())  # 아파트 게임 횟수
hand_position = list(map(int, input().split()))  # 손 위치
gyosun = list(map(int, input().split()))  # 사실상 이게 게임 횟수(교선이가 부른 수)

lose_people = []

game_start_position = deque(hand_position) # 게임 시작 직후 포지션
for i in gyosun: # 게임 시작
    for j in range(1, i): # 3이라 불렀으면 1, 2, 3 게임을 함
        game_start_position.append(game_start_position.popleft()) # 맨 아랫손을 꺼내서 맨 위로 둠
    lose_people.append(game_start_position[0]) # 맨 아랫자리에 있는 사람이 패배

print(*lose_people) # 진 사람 언패킹해서 출력