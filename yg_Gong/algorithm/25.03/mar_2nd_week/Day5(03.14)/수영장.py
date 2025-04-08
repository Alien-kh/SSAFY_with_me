# 가장 적은 비용으로 수영장을 1년간 이용할 수 있는 방법을 찾기
# 가장 적게 지출하는 비용 출력

import sys
sys.stdin = open('input.txt')

def swimming_pool_cost(cost, month_plan):
    # dp 배열
    dp= [0] * 12

    dp[0] = min(month_plan[0] * cost[0], cost[1])
    dp[1] = dp[0] + min(month_plan[1] * cost[0], cost[1])

    for i in range(2,12):
        dp[i] = min(dp[i-3] + cost[2],
                    dp[i-1] + (month_plan[i] * cost[0]),
                    dp[i-1] + cost[1])

    return dp[11]


T = int(input())
for tc in range(1, T + 1):
    cost = list(map(int, input().split()))  # 이용권 금액
    month_plan = list(map(int, input().split()))  # 수영장 계획
    dp_12 = swimming_pool_cost(cost, month_plan)
    result = min(dp_12, cost[3])

    print(f'#{tc} {result}')
