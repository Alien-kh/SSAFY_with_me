T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    
    total_profit = 0  # 총 이득을 저장할 변수
    
    for i in range(N - 1):
        for j in range(i + 1, N):  # i 이후의 날들에서 팔 수 있는 경우 찾기
            if data[j] > data[i]:  # 팔 때 이득이 있으면
                total_profit += data[j] - data[i]  # 이득을 누적
    
    print(f"#{tc} {total_profit}")