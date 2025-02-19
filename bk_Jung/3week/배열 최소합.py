def f(i, N, s):    # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    global min_v
    global cnt
    cnt += 1

    if i == N:  #
        if min_v > s:
            min_v = s
    elif min_v < s: # 중간 합계가 최소합보다 크면
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]     # 자리교환
            f(i+1, N, s + arr[i][p[i]])   # i+1자리 결정
            p[i], p[j] = p[j], p[i]     # 원상복구

T = int(input())
for test_case in range(1,T+1):
    N = int(input())    # 배열의 크기 N x N
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = [ i for i in range(N) ] # P[i] : i에서 고른 열 번호
    min_v = 10000
    cnt = 0
    f(0, N, 0)
    print(f'#{test_case} {min_v}')
