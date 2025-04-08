T = int(input())
for tc in range(1, T + 1):
    # N=사람수, M초의 시간동안 K개의 붕어빵
    N,M,K = map(int, input().split())
    # 사람들이 오는 시간 (정렬해서 받아야함)
    time = [0] + sorted(list(map(int, input().split())))
    bread = 0   # 붕어빵 수
    result = 'Possible'
    for i in range(1,N+1):
        bread = (time[i] // M) * K
        if i > bread:
            result = 'Impossible'

    print(f'#{tc} {result}')



