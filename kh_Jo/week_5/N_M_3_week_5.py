N, M = map(int,input().split())
arr = [i for i in range(1, N+1)]
check = [0] * N
result = []


def permutaion(cnt):
    if cnt == M:
        print(*result)
        return
    for i in range(N):
        if not check[i]:
            result.append(arr[i])
            permutaion(cnt+1)
            check[i] = 1
            result.pop()
            check[i] = 0
permutaion(0)