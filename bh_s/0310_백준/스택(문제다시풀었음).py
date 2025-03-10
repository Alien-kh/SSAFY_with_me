stack =[]
N = int(input())
for _ in range(N):
    stack_input = input().strip()
    
    if "push" in stack_input:
        num = stack_input.split()
        stack.append(int(num[1]))# ['push', '1'] 의 형태임.
    elif stack_input == "pop":
        print(stack.pop() if stack else -1) # 스택에 값이 있을때만. 비어있으면 -1 출력
    elif stack_input == "size":
        print(len(stack))
    elif stack_input == "empty":
        print(1 if not stack else 0)    # 스택이 비어있지 않다면 1 아니라면 0 출력
    elif stack_input == "top":
        print(stack[-1] if stack else -1)   # 스택에 값이 있다면 인덱스 -1로 접근해서 출력. 아니라면 -1출력