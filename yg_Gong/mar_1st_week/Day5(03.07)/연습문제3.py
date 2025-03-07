# 0269FAC9A0
code_bit = ['001101', '010011', '111011', '110001', '100011',
            '110111', '001011', '111101', '011001', '101111']

# 16진수를 자리별 2진수로 변환하는 함수
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
    while num10 > 0:
        i = num10 % 2
        num2 = str(i) + num2
        num10 //= 2

    while len(num2) < 4:
        num2 = '0' + num2

    return num2


arr = list(input().strip())
jinsu2 = []

for i in arr:
    num2 = jinsu(i)
    jinsu2.append(num2)
result = ''.join(jinsu2)

arr = list(result)

answer = []
strr = ''
i = 0
while i < len(arr) - 6:  # 배열의 범위
    for j in range(i, i + 6):  # 패턴의 범위
        strr += arr[j]  # 6회반복해서 패턴만들기
    if strr in code_bit:
        idx = code_bit.index(strr)
        answer.append(idx)
        i += 6
    else:
        i += 1

    strr = ''

print(*answer)
