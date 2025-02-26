# 시간초과~
# 2진수를 8진수로 변환
num = input()
# 먼저 2진수 -> 10진수로 변환
num = num[::-1]
sum_v = 0
for i in range(len(num)):
    x = int(num[i]) * 2**i
    sum_v += x
# 10진수를 8진수로 변환
x = ''
share = sum_v
while share:
    remain = share % 8  # 나머지
    share //= 8  # 몫
    x += str(remain)

print(x[::-1])  # 나머지를 거꾸로 읽으면 8진수가 됨