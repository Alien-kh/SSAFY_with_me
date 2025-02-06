#4 × 3 = 12이다.
#이 식을 통해 다음과 같은 사실을 알 수 있다.
#3은 12의 약수이고, 12는 3의 배수이다.
#4도 12의 약수이고, 12는 4의 배수이다.
#두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성


# 두 수의 관계를 확인하는 함수 정의.
def check_relationship(a, b):
    if b % a == 0: # b가 a로 나누어 떨어지는 경우 (약수)
        return "factor"
    elif a % b == 0: # a가 b로 나누어 떨어지는 경우 (배수)
        return "multiple"
    else:   # 그 외의 경우
        return "neither"

while True: # 두 수의 입력을 계속 반복하며 함수를 호출해서 출력하는 반복문
    a, b = map(int, input().split())
    if a == 0 and b == 0: # 두 수의 입력을 마지막 입력 0 0 을 할때까지 반복.
        break
    print(check_relationship(a, b))
