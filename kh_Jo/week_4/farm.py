def solve():
    middle = N //2 # 중간값
    sum_v = 0
    for r in range(middle +1):
        diff = middle - r # 중간을 기준으로 잡아주기
        for c in range(diff, N-diff): # 시작에서 1늘어나면 중간+-1 이므로 idx는 5를 기준으로 1, 4 -> 1,2,3 3에가면 0, 5 전체
            sum_v += arr[r][c]
    #위의 삼각형
    for r_2 in range(middle+1, N):
        diff = r_2 -middle # 반대 삼각형은 중간을 기준으로 얼마나 떨어졌는지  5칸이라면 3-2 = 1 칸
        for c_2 in range(diff, N-diff): # 1, 4 -> 1,2,3
            sum_v += arr[r_2][c_2]
    return sum_v


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = solve()
    print(f'#{tc} {result}')