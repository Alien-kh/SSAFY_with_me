# 고른 합 M 을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합 출력
# 입력은 고를 수 있는 경우에 대해서만 주어진다.

N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

# 모든 경우의 수 고려 및 조건문으로 알맞은 합계 뽑기.
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total = cards[i] + cards[j] + cards[k]
            if total <= M and total > max_sum:
                max_sum = total

print(max_sum)