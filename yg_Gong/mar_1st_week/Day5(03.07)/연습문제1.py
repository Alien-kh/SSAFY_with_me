#0000000111100000011000000111100110000110000111100111100111111001100111

jinsu2 = [64,32,16,8,4,2,1]

arr = list(input().strip())
code_number = int(len(arr)/7)    # 숫자의 갯수는 입력값의 길이에서 나누기 7한 값

code = [''] * code_number   # 7자리씩 묶어서 저장할 배열
jinsu10 = [0] * code_number    # 10진수로 변환한 값 저장할 배열

for i in range(code_number):    #7자리씩 묶기
    for j in range(7):
        code[i] += arr[j + (7*i)]

for k in range(code_number):    # 10진수로 변환
    for l in range(7):
        if int(code[k][l]) == 1:
            jinsu10[k] += jinsu2[l]

print(*jinsu10)

