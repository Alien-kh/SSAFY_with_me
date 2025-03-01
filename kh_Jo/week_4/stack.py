# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
N = int(input().strip())    # 첫 줄에 입력되는 명령의 수
stack = []  # 스택에 사용할 빈 배열
result = []
for _ in range(N):
    stack_input = input().strip()
    if 'push' in stack_input:
        # 와 진짜 바보다 숫자가 한자리인 경우만 생각했다,,
        # 숫자가 한자리가 아닌경우 [5]는 제대로 된 값을 못가져옴
        # stack.append(int(stack_input[5]))
        num = stack_input.split()
        stack.append(int(num[1]))
    elif stack_input == 'pop':
        if not stack:
            result.append(-1)
        else:
            result.append(stack.pop())
    elif stack_input == 'size':
        result.append(len(stack))
    elif stack_input == 'empty':
        if not stack:
            result.append(1)
        else:
            result.append(0)
    elif stack_input == 'top':
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
print(*result, sep='\n')