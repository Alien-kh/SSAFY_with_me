# 탐색 중 1 써있으면 탐색해야지 !!
# 탐색하고 있는 곳에 1적혀져 있고 and
# 탐색 시작하는 곳 -1 인덱스의 값이 0 또는 -1 인덱스의 값이 0 이라면
# 카운트 세기 시작할거임


# 카운트 후 조건 !!!
# 1개수를 센다..  k번 체크
# 개수가 K개가 되었을 때, j의 인덱스가 n - 1 이거나 또는 [i][j+1] 의 값이 0 이라면
def check(i, j): # 탐색을 시작할 좌표 전달 받음
    cnt = 0
    for x in range(K): # k번 반복하면ㅅ더 1의 개수 counting
        if lst[i][j+x]==1:
            cnt += 1 # 전달 받은 인덱스부터 K 번 확인 cnt 세기
    if cnt==K and ((j+K-1) == N-1 or lst[i][j+K] == 0): # 카운트 값이  k랑 같고 and (마지막 1이 배열의 끝이거나 또는 마지막 1 다음 값이 0이라면 )
        return 1
    else:
        return 0


testcase = int(input())
for tc in range(1, testcase+1):
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for _ in range(2):
        # 첫 번째 탐색 시 가로 탐색, 두 번째 탐색 시 세로 탐색
        for i in range(N): # 배열의 i 좌표
            for j in range(N-K+1): # 배열의 j 좌표 (탐색할 것만)
                if lst[i][j] == 1 and (j==0 or lst[i][j-1]==0): # 1 적혀있고 그리고 시작 인덱스가 0 이거나
                    # check 시작
                    answer += check(i, j)                       # 1 적혀 있는 곳 바로 앞이 0일 경우 탐색 시작
        lst = list(map(list, (zip(*lst)))) # 세로 탐색을 위해 zip으로 배열 바꿔주기

    print(f'#{tc} {answer}')