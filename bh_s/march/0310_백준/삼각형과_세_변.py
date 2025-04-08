while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break  # 종료 조건

    # 삼각형이 성립하는지 확인
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Equilateral")  # 정삼각형
        elif a == b or b == c or c == a:
            print("Isosceles")  # 두 변이 같은 경우
        else:
            print("Scalene")    # 세 변이 다른 경우
    else:
        print("Invalid")  # 삼각형을 만들 수 없음
