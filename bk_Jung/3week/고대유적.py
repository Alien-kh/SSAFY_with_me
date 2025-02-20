T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
 
    arr = [list(map(int,input().split())) for _ in range(N)]
 
    result = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:   # 1이면 카운트
                cnt += 1
            if result < cnt:    # 최대값 초기화
                result = cnt
            if i == M-1 or arr[i][j] == 0:  # 0이면 카운트 초기화
                cnt = 0
 
    cnt = 0            
    for i in range(M):
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
 
            if result < cnt:
                result = cnt
 
            if j == N-1 or arr[j][i] == 0:
                cnt = 0
 
    print(f'#{test_case} {result}')
