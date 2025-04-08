# 들어오는 값을 10진수로 변환
# 10진수를 2진수로 변환하는 함수
def jinsu(num10):
    if num10 == 'A':
        num10 = 10
    elif num10 == 'B':
        num10 = 11
    elif num10 == 'C':
        num10 = 12
    elif num10 == 'D':
        num10 = 13
    elif num10 == 'E':
        num10 = 14
    elif num10 == 'F':
        num10 = 15
    else:
        num10 = int(num10)

    num2 = ""
    while num10 > 0:          # 2진수로 변환
        i = num10 % 2         # 2로 나누기를 반복해서
        num2 = str(i) + num2  # 나머지를 num2에 저장
        num10 //= 2

    while len(num2) < 4:        # 16진수를 2진수로 변경할 땐 4자리로 맞춰야하기때문에
        num2 = '0' + num2       # 4자리수가 안된다면 앞에 0을 붙여주기

    return num2


T = int(input())

for tc in range(1, T + 1):
    N, num = input().split()
    jinsu2 = []

    for i in num:
        num2 = jinsu(i)
        jinsu2.append(num2)
    result = ''.join(jinsu2)
    print(f'#{tc} {result}')


