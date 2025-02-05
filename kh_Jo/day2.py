x = int(input()) #낸 가격을 받고
n = int(input()) # 몇 가지 항목을 구매했는지 확인
total_pay = 0 # 낸 금액과 확인하기 위해 변수 설정 (정상 처리 가격)
for _ in range(n):
    price, count = map(int, input().split()) #___ __ 형태로 주어지니 split후 int로 변환
    total_pay += price * count 
print('Yes' if total_pay == x else 'No')