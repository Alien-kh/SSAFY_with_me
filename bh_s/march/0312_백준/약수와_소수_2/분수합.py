def gcd(a, b):
    while b != 0:
        k = a % b
        a = b
        b = k
    return a

def solve(num1, num2):
    # 두 분수의 최소공배수 구하기
    return int(num1 * num2 / gcd(num1, num2))

def fraction_sum(data1, data2):
    # 공통 분모를 찾기
    common_denominator = solve(data1[1], data2[1])

    # 각 분자의 값을 공통 분모에 맞게 변환
    numerator1 = data1[0] * (common_denominator // data1[1])
    numerator2 = data2[0] * (common_denominator // data2[1])

    # 두 분자의 합 구하기
    numerator_sum = numerator1 + numerator2

    # 기약분수로 변환
    common_gcd = gcd(numerator_sum, common_denominator)
    numerator_sum //= common_gcd
    common_denominator //= common_gcd

    return numerator_sum, common_denominator

# 입력 받기
data1 = list(map(int, input().split()))  # 예: 1 2 (분수 1/2)
data2 = list(map(int, input().split()))  # 예: 2 3 (분수 2/3)

# 분수 합 계산
numerator_sum, common_denominator = fraction_sum(data1, data2)

# 결과 출력
print(numerator_sum, common_denominator)
