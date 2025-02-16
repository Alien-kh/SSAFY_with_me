def solve(a_lst, b_lst, station_lst):
    result_lst = []
    for station in station_lst: # c번 버스정류장을 기준으로
        count = 0 # 몇 개의 버스가 지나가는지
        for a, b in zip(a_lst, b_lst): # i번째 기준으로 묶어줌
            if a<= station <= b: # a[i] <= c <= b[i]
                count+=1 #버스가 지나간 수 세주기
        result_lst.append(count)  # 각 정류장 마다 지나간 버스 수 반환
    return result_lst


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A_lst = []
    B_lst = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        A_lst.append(a_i) # 추후에 왼쪽 범위
        B_lst.append(b_i) # 추후에 오른족 범위
    P = int(input()) # 정류장 개수
    station_lst = [] # 정류장 리스트에
    for j in range(1,P+1):
        c = int(input()) #정류장들을 받아서 각 정류장 마다 a[i] <=c<= b[i] 비교
        station_lst.append(c)
    result = solve(A_lst, B_lst, station_lst)
    result = ' '.join(map(str, result)) # result 리스트 받은 다음에 문자형으로 변환후 ' '랑 join
    print(f'#{tc} {result}')