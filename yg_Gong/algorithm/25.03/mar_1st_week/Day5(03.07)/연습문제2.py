# 1D06079861D79F99F

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
    while num10 > 0:  # 2진수로 변환
        i = num10 % 2  # 2로 나누기를 반복해서
        num2 = str(i) + num2  # 나머지를 num2에 저장
        num10 //= 2

    while len(num2) < 4:  # 16진수를 2진수로 변경할 땐 4자리로 맞춰야하기때문에
        num2 = '0' + num2  # 4자리수가 안된다면 앞에 0을 붙여주기

    return num2

arr = list(input().strip())
jinsu2 = []

for i in arr:
    num2 = jinsu(i)
    jinsu2.append(num2)
result = ''.join(jinsu2)


jinsu2 = [64,32,16,8,4,2,1]
arr = list(result)
code_number = int(len(arr)/7)    # 숫자의 갯수는 입력값의 길이에서 나누기 7한 값
namuji = int(len(arr) % 7)      # 7개씩 묶고 나머지
code = [''] * code_number   # 7자리씩 묶어서 저장할 배열
jinsu10 = [0] * code_number    # 10진수로 변환한 값 저장할 배열

for i in range(code_number):    #7자리씩 묶기
    for j in range(7):
        code[i] += arr[j + (7*i)]

for k in range(code_number):    # 10진수로 변환
    for l in range(7):
        if int(code[k][l]) == 1:
            jinsu10[k] += jinsu2[l]

if namuji > 0:
    namuji = result[-namuji:]
one_count = namuji.count('1')   # 떼어낸 나머지에서 1의 갯수 세기

namuji10 = 0
for i in range(one_count):  # 1의 갯수만큼 2의 제곱 더하기
    namuji10 += 2 ** i
jinsu10.append(namuji10)

print(*jinsu10)