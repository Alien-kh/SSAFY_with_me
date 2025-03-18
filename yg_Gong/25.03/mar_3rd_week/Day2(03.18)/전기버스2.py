# 배터리를 교체하는 함수
def change_charger():




T = int(input())
for tc in range(1, T + 1):
    charger = list(map(int, input().split()))
    N = charger[0]  # 정류장 수
