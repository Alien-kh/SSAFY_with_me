
# 영수증의 총 금액 입력받기
total_money = int(input())

# 구매한 물건 종류
items = int(input())

# 금액을 비교하려면?? 다른 변수 하나 더 필요하다.
compare_money = 0

for _ in range(items): # 0부터 items-1 까지.
    i, j = map(int, input().split()) # 물건 가격 i , 물건 개수 j
    compare_money += i*j # 물건 가격 * 물건 개수 -> 해당 물건들의 금액. 반복문으로 다 더한 뒤 총액과 비교.

if compare_money == total_money: # 직접 계산한 금액과 영수증의 총액 비교.
    print('YES')
else:
    print('NO')
    