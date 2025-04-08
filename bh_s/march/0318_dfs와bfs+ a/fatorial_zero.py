N = int(input())

def count_trailing_zeros(n):
    count = 0
    while n >= 5:
        n //= 5  # 5의 배수를 찾기 위해 n을 5로 나눔
        count += n  # 나눈 몫을 누적 (5의 배수의 개수만큼 0이 추가됨)
    return count

print(count_trailing_zeros(N))
