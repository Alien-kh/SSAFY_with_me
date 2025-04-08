T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # N, A 가 무조건 작도록 만들면 더 편하다.
    if N > M:
        N, M = M, N
        A, B = B, A

    max_result = -1e9 # -1억.
    # 문제에서 볼 수 있는 중심이 되는 반복문
    # -> 작은 리스트가 큰 리스트의 범위 안에서 1칸씩 진행하는 것.
    # -> 범위를 넘어가지 않으려면 어디까지 생각해야 할까?
    for long_idx in range(M-N+1): # 큰 리스트 길이 - 작은리스트 + 1
        result = 0
        for short_idx in range(N):
            result += A[short_idx] * B[long_idx + short_idx]
        
        max_result = max(max_result, result)
        
    print(f"#{tc} {max_result}")