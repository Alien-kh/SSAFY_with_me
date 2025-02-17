# 예전에 프로그래머스 스택 코드 (후위 연산자 테스트 할 겸 사용해봄)
class ArrayStack: # 스택을 만들어서
    def __init__(self):
        self.data = []

    def size(self): # 사이즈를 리턴 해준다던지
        return len(self.data)

    def isEmpty(self): # 비어있는지 확인해준다던지
        return self.size() == 0

    def push(self, item): # 푸쉬하고
        self.data.append(item)

    def pop(self): # 팝하고
        return self.data.pop()

    def peek(self):
        return self.data[-1]





def solution(S):
    opStack = ArrayStack()  # 연산자를 담을 스택
    output = []  # 후위 표기법 식을 담을 리스트

    for char in S:
        # 피연산자(숫자)인 경우 결과 리스트에 바로 추가
        if char.isdigit():
            output.append(char)

        # 2. '(' 일 경우 스택에 push
        elif char == '(':
            opStack.push(char)

        # 3. ')' 일 경우 '('가 나올 때까지 스택에서 pop하여 결과에 추가
        elif char == ')':
            topToken = opStack.pop()
            while topToken != '(':
                output.append(topToken)
                topToken = opStack.pop()

        # 4. 연산자(+ - * /)일 경우
        else:# '+' 연산자
            # 스택에 남아 있는 '+'를 모두 pop (왼쪽 결합성을 위해)
            while not opStack.isEmpty() and opStack.peek() == '+':
                output.append(opStack.pop())
            opStack.push(char)

    # 5. 스택에 남아 있는 연산자를 모두 pop하여 결과에 추가
    while not opStack.isEmpty():
        output.append(opStack.pop())

    # 리스트를 문자열로 합쳐서 반환
    return ''.join(output)
def evaluate_postfix(postfix): # 후위 연산자 계싼
    stack = []
    for token in postfix:
        if token.isdigit(): # 만약에 숫자면 스택에 추가하고
            stack.append(int(token))
        else:  # 연산자 '+'만 처리 # + 일 떄 뒤에서 2개 빼서 하나로 더해주고 다시 return
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
    return stack[0]

T = 10
for tc in range(1, T+1):
    N= int(input())
    expr = input().strip()  # 입력받은 중위표현식
    postfix_expr = solution(expr)
    result = evaluate_postfix(postfix_expr)
    print(f'#{tc} {result}')
