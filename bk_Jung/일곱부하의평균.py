T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = list(map(int,input().split()))

    N = len(arr)
    max_arr = 0
    sum_arr = 0
    for i in arr:
        sum_arr += i
    for i in arr:
        if max_arr < i:
            max_arr = i
    
    max_arr += 1
    while True:
        if (sum_arr + max_arr) % (N+1) == 0:
            break
        else:
            max_arr += 1

    print(max_arr)        
