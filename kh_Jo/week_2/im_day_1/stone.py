testcase = int(input())
for tc in range(1, testcase+1):
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))

    for _ in range(M):
        i,j = map(int, input().split())
        i -=1 # 기준 돌의 인덱스 값 구하기
        for k in range(1, j+1): #  기준으로 부터 얼만큼 떨어졌는가
            left = i-k
            right = i + k
            if left<0 or right == len(lst):break # 배열 범위 벗어나면 비교 중단/ break하면 가장 가까운 반복문만 꺼짐
            if lst[left]==lst[right]: # 비교하는 돌의 색이 같으면 돌 색상 바꿔주기
                lst[left]= 1-lst[left] # 만약에 0이면 1-0 이니깐 1로 바뀌고
                lst[right]= 1-lst[right] # 만약에 1이면 1-1 이니깐 0으로 바뀐다.



    print(f'#{tc}',*lst)