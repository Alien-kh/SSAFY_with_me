# 백준 0의 개수

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    # N이 M보다 크면 교환
    if N > M:
        N, M = M, N

    count = 0

    for num in range(N, M + 1):
        for char in str(num):
            if char == '0':
                count += 1
    print(count)