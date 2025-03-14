# level :12월 (12 초과일 때 종료)
# branch : 4개 (1일 (다음 달 체크), 1달( 다음 달 체크), 3달 ( 현재 달 + 3), 1년( +12)
import sys

sys.stdin = open('input.txt', 'r')




T = int(input())
for tc in range(1, T + 1):
    # 이용권 가격들 (1일 , 1달, 3달, 1년)
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
    # 12개월 이용 계획
    days = [0] + list(map(int, input().split()))  # index를 1부터 접근하는게 편리하기에 버리는 0월 만들어 주기

    dp = [0] * 13
    # 시작점 초기화 (1월, 2월)
    # 1월의 가격 (1일권 구매, 1달권 구매)
    dp[1] = min(days[1] * cost_day, cost_month)
    # 2월의 가격 = 1월의 가격 + (1일권 구매 vs 1달권 구매)
    dp[2] = dp[1] + min(days[2] * cost_day, cost_month)

    # 3월 12월은 반복하면석 ㅖ산
    for month in range(3, 13):
        # N 월의 최소 비용
        # 1. (N-3)월에 3개월 이용권을 구입한 경우
        # 2. (N-1)월의 최소 비용 + 1일권 구매
        # 3. (N-1)월의 최소 비용 + 1달권 구매
        dp[month] = min(dp[month-3] + cost_month3 , dp[month-1] + (days[month] * cost_day), dp[month-1] + cost_month)

    # 12월의 누적 최소 금액 vs 1년권
    answer = min(dp[12], cost_year)
    print(f'#{tc} {answer}')

    # 전체적인 문제
    # 1. TOP-DOWN 방식
    # - DP(메모이제이션)
    # - 거듭제곱 문제
    # 2. Bottom-UP 방식
    # - 시작점을 정해둔다.
    # - 앞으로 쌓아 나아가면서 진행
    #   - 기존 값을 활용
    #   - 가장 좋은 값을 계산해서 저장하면서 진행
    # -> 점화식을 구하는 경우가 많다.