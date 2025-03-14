import sys
sys.stdin = open('input.txt', 'r')

# level: 점운 수
# branch : 탑에 포함 시킨다 or 안 시킨다
def recur(cnt, total_height):
    global  answer
    # 기저조건 가지치기
    # 이미 B 이상인 탑이면, 점원을 더 쌓을 필요가 없다.
    # => 탑이 더 높은 정답은 필요 없다.
    if total_height >= B:
        answer = min(answer, total_height)
        return



    if cnt == N:
        return
    recur(cnt + 1, total_height + heights[cnt])     # 포함 시키는 경우
    recur(cnt + 1, total_height)    # 탑에 포함 안 시키는 경우


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    answer = int(21e8)
    recur(0, 0)
    print(f'#{tc} {answer - B}')