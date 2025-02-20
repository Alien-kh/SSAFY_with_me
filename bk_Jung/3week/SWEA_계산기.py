def forth(arr):
    stack = []
    for i in arr:
        stack.append(i)
    
    while stack:
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
        if len(stack) == 1:
            return stack.pop()

T = 10
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split('+')))
    print(f'#{test_case} {forth(arr)}')

