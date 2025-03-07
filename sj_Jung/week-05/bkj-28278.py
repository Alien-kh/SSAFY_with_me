import sys

command_num = int(sys.stdin.readline()) # 명령 갯수

stack = [] # 스택
top = -1 # 스택의 가장 윗 값 인덱스

for cn_idx in range(1, command_num+1):
    command_input = list(sys.stdin.readline().split()) # 명령 입력

    if command_input[0] == '2': # 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        if top == -1:
            print(-1)
        else:
            print(stack.pop())
            top -= 1
    elif command_input[0] == '3': # 3: 스택에 들어있는 정수의 개수를 출력한다.
        print(len(stack))
    elif command_input[0] == '4': # 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
        if top == -1:
            print(1)
        else:
            print(0)
    elif command_input[0] == '5': # 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        if top == -1:
            print(-1)
        else:
            print(stack[len(stack)-1])
    else: #  X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
        stack.append(command_input[1])
        top +=1
