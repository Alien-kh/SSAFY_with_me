def solve(l, r, num):
    cnt = 0
    while True:
        c = int((l+r)/2)
        if c < num:
            cnt +=1
            l = c
        elif c > num:
            cnt += 1
            r = c
        else: # 찾았을 경우
            return cnt

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split()) # P 전체 페이지 A 찾아야 하는 수, B 찾아야 하는 수2
    l_A, r_A = 1, P
    l_B, r_B = 1, P
    result_A = solve(l_A, r_A, A)
    result_B = solve(l_B, r_B, B)
    winner = 'A'
    if result_A > result_B:
        winner = 'B'
    elif result_A == result_B:
        winner = 0
    print(f'#{tc} {winner}')


'''
3
400 300 350
1000 299 578
1000 222 888
'''