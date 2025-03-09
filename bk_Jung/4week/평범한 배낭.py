def dp(N,M,memo):
    for i in range(N):
        for w in range(M,W[i] -1, -1):
            c = memo[w - W[i]] + V[i]
            memo[w] = max(memo[w],c)

    return memo[M]

N,M = map(int,input().split())

memo = [0] * (M+1)
W = []
V = []
for i in range(N):
    a,b = map(int,input().split())
    W.append(a)
    V.append(b)

print(dp(N,M,memo))