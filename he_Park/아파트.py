# 똑같은 풀이인데 함수를 사용하니 시간이 2배로 줄어든다.  # 이유는 모름
def solve(num):
    global current
    for _ in range(num):
        current = (current + 1) % len(hands)  # 끝에 도달하면 처음 위치로

N = int(input())
T = int(input())
hands = list(map(int, input().split()))
call_num = list(map(lambda x : int(x)-1, map(int, input().split())))

current = 0

for i in call_num:
    solve(i)
    print(hands[current], end= ' ')