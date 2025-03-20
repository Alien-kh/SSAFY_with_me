import sys
sys.stdin = open('백만_장자_프로젝트.txt')

T = int(input())  # 테스트 케이스
for tc in range(1, T + 1):
    N = int(input())  # 날의 수
    prices = list(map(int, input().split()))  # 일별 매매가

    max_price = 0  # 현재까지의 최고 가격
    profit = 0  # 총 이익

    # 뒤에서부터 가격을 탐색
    for i in range(N - 1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]  # 최고 가격 갱신
        else:
            profit += max_price - prices[i]  # 현재 가격보다 최고 가격이 크다면 차익을 얻음

    print(f'#{tc} {profit}')
