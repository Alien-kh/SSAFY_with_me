n = int(input())

# 피보나치 함수 정의
def Fibo(num):
    # 조건문으로 초기 num 들에 대한 예외 사항을 줘야 한다.
    # num이 0일때는 0, num이 1 또는 2일때는 1이 나와야 한다.
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    return Fibo(num-1) + Fibo(num-2)

print(Fibo(n))