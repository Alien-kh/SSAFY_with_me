# 초기 점 4개. 1번 연산 실행 -> (4 + 5) = 9
# 규칙성을 띈다. 초기 값 2의 제곱. 처음 연산시 3의 제곱. 2번째에는 5의 제곱

def solve(N):
    value = (1+2**N)**2

    return value

N = int(input())
print(solve(N))