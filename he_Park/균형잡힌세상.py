while True:
    txt = input()
    ans = 'yes'
    if txt == '.':  # 입력 종료 조건
        break
    top = -1
    stack = [0] * 100
    dic = {')': '(', ']':'['}
    for x in txt:
        if x == '(' or x == '[':  # 여는 괄호 push
            top += 1
            stack[top] = x
        elif x == ')' or x == ']':
            if stack[top] == dic[x]:
                top -= 1
            else:  # 비어있거나 짝이 맞지 않으면
                ans = 'no'
                break
    if top > -1:  # 여는 괄호가 남아있으면
        ans = 'no'
    print(ans)