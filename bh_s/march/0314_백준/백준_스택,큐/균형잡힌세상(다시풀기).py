def check(txt):

    # 괄호 짝 확인
    top = -1    # 스택의 제일 위를 보는 포인터
    stack = []
    check_dict = {')': '(', ']': '['}

    ans = 'yes' # 기본 대답은 yes
    for x in txt:
        if x in '([':
            top += 1
            stack.append(x)
        elif x in ')]':
            if top == -1 or stack[top] != check_dict[x]:
                ans = 'no'
                break
            else:   # 짝이 맞아서 스택에서 제거하는 경우
                top -= 1
                stack.pop()

    if top > -1:    # 행동이 끝나고 스택에 값이 남아있는 경우
        ans = 'no'
    return ans  # 모든 경우가 끝나고 ans 리턴.


def lines():

    line_s = []   # 결과 저장 리스트
    while True:
        line = input().rstrip()
        if line == '.':
            break
        if len(line) > 100 or not line.endswith('.'):   # 온점(.) 으로 끝나는 지 확인
            continue
        line_s.append(check(line[:-1]))  # 마지막 온점 제외하고 검사.
    print('\n'.join(line_s))


lines()
