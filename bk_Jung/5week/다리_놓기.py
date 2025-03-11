t = int(input())
for tc in range(t):
    a,b = map(int,input().split())
    M = 1
    N = 1
    N_2 = 1
    for i in range(1,a+1): # 조합 계산
        M *= i  # r!

    for i in range(1,b+1): # n!
        N *= i
    
    for i in range(1,(b-a+1)): # n-r!
        N_2 *= i

    result = N // M // N_2
    print(result)