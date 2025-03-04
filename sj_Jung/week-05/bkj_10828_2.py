import sys

testcase = int(sys.stdin.readline())

stack = []
for _ in range(testcase):
    input_commend = sys.stdin.readline().split()

    if input_commend[0] == 'pop':
        if len(stack) < 1:
            print('-1')  # 없으면 -1
        else:
            print(stack.pop())  # 있으면 그 값을 pop 하고 top -1
    elif input_commend[0] == 'size':
        print(len(stack))  # 현재 사이즈는 top+1(top은 현재 스택 제일 윗값의 인덱스(주소값)이므로 항상 1이 적다. 따라서 1 더하면 지금 현재 저장값이다)
    elif input_commend[0] == 'empty':
        if len(stack) == 0:
            print('1')  # 비어있으면 1
        else:
            print('0')  # 뭔가 있으면 0
    elif input_commend[0] == 'top':
        if len(stack) < 1:
            print('-1')  # 없으면 -1
        else:
            print(stack[len(stack)-1])  # 스택의 탑값을 인덱스로 불러와서 출력
    else:
        stack.append(input_commend[1])  # push 하고 top +1