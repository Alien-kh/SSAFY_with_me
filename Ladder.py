T = 10

for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int,input().split()))) # 사다리 넣기

    for i in range(100):
        if arr[99][i] == 2:
            start = i  # 시작 좌표
    
    dx = [0,0,-1]
    dy = [1,-1,0]
    d = 0
    r = 99
    c =  start #시작 좌표
    
    while r > 0:
        for i in range(2):
            



    

    