num1 = int(input())
num2 = int(input())

# num2의 각 자리 숫자를 분리
num2_digits = [int(digit) for digit in str(num2)]

# 각 자리 숫자로 곱한 값
num3 = num1 * num2_digits[2]  # 1의 자리
num4 = num1 * num2_digits[1]  # 10의 자리
num5 = num1 * num2_digits[0]  # 100의 자리

# 최종 곱셈 결과
num6 = num1 * num2

# 출력
print(num3)
print(num4)
print(num5)
print(num6)
