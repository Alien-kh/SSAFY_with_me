# 최대공약수(GCD) 구하기 (유클리드 호제법 사용)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 입력 받기
n = int(input())
positions = [int(input()) for _ in range(n)]

# 가로수 간의 간격 구하기(리스트에 저장)
diffs = []
for i in range(1, n):
    diffs.append(positions[i] - positions[i - 1])

# 모든 간격의 최대공약수 구하기
common_gcd = diffs[0]
for i in range(1, len(diffs)):
    common_gcd = gcd(common_gcd, diffs[i])

# 추가로 심어야 하는 나무 수 계산
total_trees = 0
for diff in diffs:
    total_trees += (diff // common_gcd) - 1

print(total_trees)
