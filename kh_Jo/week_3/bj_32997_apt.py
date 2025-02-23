from collections import deque
N = int(input()) # 인원
T = int(input()) # 아파트 게임 횟수
q = deque(input().split()) # deque을 만들어서 그 안에 손 순서 넣어주기
result = [] # 진 사람들을 담을 리스트
game_lst = list(map(int, input().split()))
for game in game_lst: # 게임 횟수 만큼 반복
    for i in range(game-1):
        hand = q.popleft()
        q.append(hand) # 부른 숫자-1만큼 손을 빼서 위로 올려줌
    result.append(q[0]) # 부른 숫자
print(*result)

