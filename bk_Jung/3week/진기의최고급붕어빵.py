T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M,K = map(int,input().split())
    arr = (list(map(int,input().split())))
    arr.sort()
    rest = [0] * (max(arr) +1)
    z = False
    if arr[0] == 0:
        z = True
 
    for i in arr:
        rest[i] -= 1
 
 
    for i in range(1,len(rest)):
        if i % M == 0:
            rest[i] += K
    result = [0] * (max(arr)+1)
 
    for i in range(1,len(rest)):
 
        result[i] = result[i-1] + rest[i]
 
 
    for i in result:
        if i < 0 or z:
            print(f'#{test_case} Impossible')
            break
    else:
        print(f'#{test_case} Possible')