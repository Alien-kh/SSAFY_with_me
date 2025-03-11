# 세 막대로 삼각형 만들기
# 세 변은 1<= a,b,c <= 100
# 삼각형의 둘레는 최대가 되어야 한다.

a, b, c = map(int, input().split())

if a + b > c and a + c > b and b + c > a:
    print(a+b+c)

elif a >= b + c:
    a = b + c - 1
    print(a+b+c)

elif b >= a + c:
    b = a + c - 1
    print(a + b + c)

elif c >= a + b:
    c = a + b - 1
    print(a+b+c)
