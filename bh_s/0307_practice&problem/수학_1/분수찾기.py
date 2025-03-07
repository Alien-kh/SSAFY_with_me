# 무한히 큰 배열에 분수가 적혀있다고 생각.
# [1/1][1/2][1/3] .....
# [2/1][2/2][2/3]
# [3/1][3/2][3/3]
# 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 순으로 지그재그 순서가 n 번째 분수
# X값 입력 했을 때, 이 X 번째 분수를 찾기.

X = int(input())

# 몇 번째 대각선인지 찾기
n = 1
while (n *(n+1)) // 2 < X:
    n += 1


# 해당 대각선의 시작 번호
start = (n * (n-1)) // 2 + 1
pos = X - start    # (대각선에서 위치)

# 대각선이 홀수면 분자 감소 , 분모 증가
# 대각선이 짝수면 분자 증가 , 분모 감소
if n % 2 == 1:
    numerator = n - pos
    denominator = pos + 1
else:
    numerator = pos + 1
    denominator = n - pos

print(f'{numerator}/{denominator}')
