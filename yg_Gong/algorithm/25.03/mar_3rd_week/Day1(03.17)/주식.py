import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())    # 날의 수
    stock = list(map(int, sys.stdin.readline().split()))

    max_price = 0   # 주식최고가
    profit = 0      # 순수익

    for i in range(N-1, -1, -1):
        if stock[i] > max_price:
            max_price = stock[i]
        else:
            profit += max_price - stock[i]


    print(profit)