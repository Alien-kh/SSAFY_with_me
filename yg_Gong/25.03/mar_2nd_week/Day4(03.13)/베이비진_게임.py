# 12장의 카드를 2명이서 번갈아가며 뽑음
# 연속인 숫자가 3개이상이면 run
# 같은 숫자가 3개 이상이면 triplet

# run을 판단하는 함수
def runn(arr):

    if len(arr) >= 3:
        arr2 = sorted(set(arr))
        for i in range(len(arr2) - 2):
            if arr2[i] + 1 == arr2[i + 1] and arr2[i + 1] + 1 == arr2[i + 2]:
                return True
    return False    # 연속적인 숫자가 3개이상없거나 아직 3개이상의 카드가 없을 때 함수 종료

# triplet을 판단하는 함수
def triplet(arr):
    arr.sort()
    if len(arr) >= 3:
        for i in range(len(arr) - 2):
            if arr[i] == arr[i+1] == arr[i+2]:
                return True
    return False

# 승자 판별 및 게임 진행하는 함수
def play_game(cards, player1, player2, turn=0):

    if turn == len(cards):
        return 0  # 비김

    # 카드분배
    if turn % 2 == 0:
        player1.append(cards[turn])
    else:
        player2.append(cards[turn])

    # run 이나 triplet이 달성한 player가 있는지 확인
    if runn(player1) or triplet(player1):
        return 1  # player1 승리
    if runn(player2) or triplet(player2):
        return 2  # player2 승리

    # 다음 턴 진행
    return play_game(cards, player1, player2, turn + 1)

# 입력 및 실행
T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    player1=[]
    player2=[]
    result = play_game(cards,player1,player2)
    print(f'#{tc} {result}')