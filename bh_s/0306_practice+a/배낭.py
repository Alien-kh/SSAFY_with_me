def solve(N, K, item):
    # dp[i] : 무게가 i일 때 얻을 수 있는 최대 가치
    dp = [0] * (K + 1)

    # 모든 아이템에 대해
    for i in range(N):
        weight, value = item[i]

        # 뒤에서부터 진행하여 이전에 계산된 값을 덮어쓰지 않도록 함
        for w in range(K, weight - 1, -1):
            # 무게가 w일 때, 현재 아이템을 선택할 경우를 비교
            dp[w] = max(dp[w], dp[w - weight] + value)

    # 최대 가치 반환
    return dp[K]


# 입력 받기
N, K = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
result = solve(N, K, item)
print(result)
