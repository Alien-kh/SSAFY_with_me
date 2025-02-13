# 두 개의 숫자열
def solve(arr_A, arr_B):
    n = 0
    m = 0
    a = []
    b = []
    max_value = 0

    if len(arr_A) > len(arr_B):     # 어떤 배열이 더 긴지 확인
        n = len(arr_A)
        m = len(arr_B)
        a, b = arr_A, arr_B
    else:
        n = len(arr_B)
        m = len(arr_A)
        a, b = arr_B, arr_A

    for i in range(n - m + 1):
        sum_value = 0
        for j in range(m):
            sum_value += a[i + j] * b[j]    # 마주보는 숫자곱해서 sum에 넣어주기

        max_value = max(max_value, sum_value)  # 최댓값

    return max_value  # 결과 반환


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = solve(A, B)

    print(f'#{tc} {result}')
