N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(input()))
# dp 테이블 만들어주기 (안올라갔을 때(2번 연속 밟았을 때 다음 칸을 밟으면 안되고 다다음칸 밟아야됨), 1칸, 2칸연속)
dp = [[0]*3 for _ in range(N+1)]
for i in range(1, N+1): # 1번칸부터 시작
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) # 이전에 밟은 것들 중(1칸 연속, 2칸 연속 중 최대값)
    dp[i][1] = dp[i-1][0] + stairs[i] # 이전에 안밟고, 이번에 밟아서
    dp[i][2] = dp[i-1][1] + stairs[i] # 이전에 밟고, 또 밟으니깐
ans = max(dp[N][1], dp[N][2]) # 골라야하는 것은 결국 밟은 것들 중에서
print(ans)