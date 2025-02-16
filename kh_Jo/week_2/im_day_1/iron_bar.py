def solve():
    top = -1 # 봉의 개수
    N = len(bar)
    stack = []
    cnt = 0
    prev = '' # 스택의 이전 문자
    # 만약에 (가 연속으로 나오면 긴 막대기 위에 보다 짧은 막대기
    # 만약에 (이후에 ) 라면 레이저
    # 만약에 ) 이후에 ) 가 나오면 쇠막대기 끝
    for x in bar:
        if x == '(': # 만약에 (가 나오면 일단 스택이 넣어주기
            stack.append(x)
            # 두 번째 만약 '('를 만나면 봉의 개수가 늘어남 (위에 하나 더 생성)
        else:
            # 첫 번째 만약 바로 ')'를 만나면 레이저
            if prev == '(':
                stack.pop()
                cnt += len(stack) # 봉의 개수 만큼 늘어난다 (만약 봉이 3개라면 반갈하면 6개)
            # 만약 ')' 뒤에 ')가 나오면 막대기가 끝난 거임)
            else:
                stack.pop()
                cnt += 1 # 마지막 조각이므로 1개 더해주기 (남은 것)
        prev = x # 추후에 비교를 위해서 마지막 문자 저장
    return cnt


T = int(input())
for tc in range(1, T+1):
    bar = list(input())
    result = solve()
    print(f'#{tc} {result}')