# tip) 문제 시뮬레이션이 홀수 > 짝수 경우를 잘 생각하기! (그 반대도)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split())
    # print(arr)
    # 0 1 2, 3 4 5
    arr_l = arr[ : (N + 1) // 2]
    arr_r = arr[(N + 1) // 2 : ]

    print(f'#{tc}', end=' ')
    for i in range(N//2):
        print(f'{arr_l[i]} {arr_r[i]}', end=' ')

    if N % 2 != 0:
        print(arr_l[-1], end=' ')

    print()