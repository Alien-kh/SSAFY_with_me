def permutation(idx):
    global min_result,result
    if result > min_result:
        return
    if idx == N:
        if result < min_result:
            min_result = result
        return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            result += arr[idx][i]
            permutation(idx + 1)
            used[i] = 0
            result -= arr[idx][i]



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    used = [0] * (N+1)
    min_result = 1e11
    result = 0
    permutation(0)
    print(f'#{tc} {min_result}')

    