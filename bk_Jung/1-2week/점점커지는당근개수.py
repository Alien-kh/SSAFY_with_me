T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    result = 0
    cnt = 1
    for i in range(N-1):
        if arr[i] < arr[i+1]:
            cnt+=1
        else:
            cnt = 1

        if result < cnt:
            result = cnt
        

    print(f'#{test_case} {result}')
 