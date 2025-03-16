
def stair(N, cnt):
    dp = [0] * (N + 1)

    # 첫 번째 계단 선택하는 경우
    dp[1] = lst[1]

    if N > 1:   # N 이 1보다 커야 선택지의 경우가 생김
        # 두 번째 계단을 밟는 경우
        dp[2] = lst[1] + lst[2]

    # 세 번째 계단부터 점화식 사용 가능
    for j in range(3, N + 1):
        # i번째 계단은 2가지 경우로 볼 수 있다. 2칸으로 바로 온 경우 or 3칸 전에서 2칸 뛰고 1칸 더 올라온 경우
        dp[j] = max(dp[j-2] + lst[j], dp[j-3] + lst[j-1] + lst[j])

    return dp[N]


N = int(input())
lst = [0] * (N + 1)
for i in range(1, N+1):
    lst[i] = int(input())

print(stair(N, lst))
