def forth(arr):
    stack = []
    for i in arr:
        if i.isdigit():
            stack.append(int(i))
        elif i in '+-*/':
            if len(stack) < 2:
                return 'error'
            else:    
                b = stack.pop()
                a = stack.pop()
                if i == '+':        
                    stack.append(a + b)
                elif i == '-':   
                    stack.append(a - b)
                elif i == '*':        
                    stack.append(a * b)
                elif i == '/':    
                    stack.append(a // b)
        elif i == '.':
            if len(stack) == 1: 
                return stack.pop()
            else:
                return 'error'

T = int(input())
for test_case in range(1,T+1):
    arr = list(input().split())
    result = 0
    print(f'#{test_case} {forth(arr)}')
