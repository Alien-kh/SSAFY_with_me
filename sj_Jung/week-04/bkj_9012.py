def stack_machine(par_text):

    global answer, top

    if par_text == '(': # 만약 여는 괄호라면
        stack.append(par_text) # 스택에 추가
        top += 1 # 스택의 제일 높은 위치 갱신
        return answer
    elif par_text == ')': # 만약 닫는 괄호라면
        if top < 0: # 스택이 비어있는데 추가할려하면 불균형 하므로 No 리턴
            answer = 'NO'
            return answer
        else: # 스택이 있다면
            stack.pop() # 꺼내고
            top -= 1 # 제일 높은 위치 갱신
            return answer

testcase = int(input())

for _ in range(testcase):
    par_input = input()

    stack = [] # 초기 설정: stack
    top = -1  # 초기 설정: top
    answer = 'YES' # 초기 설정: answer

    for i in par_input:
        answer = stack_machine(i) # 답 입력 받음, def 호출
        if answer == 'NO': # 이미 NO로 판단되었다면 break.
            break

    if top != -1: # 스택이 남아있다면 불균형하므로 NO
        answer = 'NO'

    print(answer)