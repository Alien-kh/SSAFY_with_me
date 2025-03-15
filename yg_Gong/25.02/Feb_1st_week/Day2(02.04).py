# 영수증

# 첫줄에는 총금액 X 가 주어진다
# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
# 이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.

X = int(input())
N = int(input())

# 입력값을 저장할 list 생성
bill = []

# 금액 합산을 저장할 변수 생성
total = 0

# N만큼 값 입력 반복
for num in range(N):
    a,b = map(int, input().split())
    bill.append(dict(price = a, cnt = b)) # 입력값 a,b를 dict형태로 bill list에 append
    total +=  a * b  # 입력값을 total 변수에 합산

if total == X :
    print('Yes')
elif total != X:
    print('No')
