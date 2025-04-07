def permutaion(idx,result):
    global max_result
    if result < max_result:
        return
    if idx == N:
        if max_result < result:
            max_result = result
        return

    for i in range(N):
        if not used[i] and arr[idx][i]:
            used[i] = 1
            permutaion(idx + 1,result * arr[idx][i]*0.01)
            used[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    used = [0] * (N+1)
    max_result = 0
    permutaion(0,1)
    print(f'#{tc} {max_result*100 :.6f}')