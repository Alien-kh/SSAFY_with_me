
N = int(input())
dp = [[0] * (N+1) for _ in range(2)]
stair = [int(input()) for _ in range(N)]


dp[1][1] = stair[0]
if N >= 2:
    dp[0][2] = stair[1] + stair[0]
    dp[1][2] = stair[1]

for i in range(3,N+1):
    dp[0][i] = dp[1][i-1] + stair[i-1]
    dp[1][i] = max(dp[0][i-2], dp[1][i-2]) + stair[i-1]

print(max(dp[0][N],dp[1][N]))