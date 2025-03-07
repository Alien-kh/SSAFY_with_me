

def dp():
    for i in range(N):
        for w in range(100,L[i]-1,-1):
            memo[w] = max(memo[w],memo[w- L[i]] + J[i])
    return memo

N = int(input())
L = list(map(int,input().split()))
J = list(map(int,input().split()))
memo = [0] * 1000
dp()
max_num = 0
for i in range(99,0,-1):
    if memo[i] > max_num:
        max_num = memo[i]

print(max_num)