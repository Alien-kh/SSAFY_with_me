def solve(N, M):
    lst =[]
    for i in range(1,N+1):
        if N % i == 0:
            lst.append(i)
    if M > len(lst):  # 인덱스를 초과하는 경우 0 반환
        return 0
    return lst[M-1]

N, M= map(int, input().split())
print(solve(N,M))
