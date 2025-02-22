# 아파트 게임, 백준 실버 5

def aprtment_game(hand, cnt):
    # 교선이가 부르는 아래에서 cnt 번째가 패배한다.
    # cnt 만큼 회전해서 0번째로 패배자를 빼내면 front에서 빼내면서, queue로 보이겠지?
    # 실습 '회전' 참고하면 더 좋다.
    turn = (cnt - 1) % len(hand)    # # cnt는 인덱스 + 1 인걸 생각하자.
    for _ in range(turn):
        hand.append(hand.pop(0))
    # 회전 후의 첫 번째(0번 인덱스)가 패배자.
    loser = hand[0]
    return loser, hand

N = int(input())
T = int(input())
hand = list(map(int, input().split()))
b_j = list(map(int,input().split()))


result = []     # 패배한 사람들을 기록하기 위한 리스트.
for cnt in b_j: # 사실 b_j 의 크기가 곧 T 이니까 T값을 받는 의미가.... 있나? 리스트에서 꺼내서 반복
    loser, hand = aprtment_game(hand, cnt) # 함수 호출 및 언패킹
    result.append(loser) # 패배자 정보를 순서대로 append.

print(*result)

#   print(' '.join(map(str, result)))   공백을 기준으로, 원하는 패배자 번호를 '문자열'로 출력