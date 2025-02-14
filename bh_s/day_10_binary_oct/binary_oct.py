'''
주의 !!!!!! 2진수는 문자열로 받아야 한다. 숫자형태의 데이터로 받으면 문제가 발생한다.
'''
def binary_oct(binary):
    binary_list = list(binary)
    length = len(binary_list)


    # 3자리씩 끊어서 만들면 8진수로 변환하기 쉬워짐으로 3으로 나누어 떨어지게 만들기.
    temp = []
    while (length + len(temp)) % 3 != 0:
        temp += ['0']

    binary_list = temp + binary_list    # 변환을 위해 앞쪽에 0을 붙인 2진수
    length = len(binary_list)   # 새롭게 구하는 길이

    oct_list = []
    for i in range(0, length, 3):   # 3자리씩 변환시키자.
        convert = binary_list[i:i+3]

        # 2진수 3자리씩 10진수로 만들기

        value = 0
        if convert[0] == '1':
            value += 4
        if convert[1] == '1':
            value += 2
        if convert[2] == '1':
            value += 1

        oct_list += [value]
    
    return oct_list

num = input()
print(*binary_oct(num), sep='') # sep 이라는 기능을 알아보자. 이러면 314 나옴.
                                # sep : 분리해서 출력. ''안의 내용물로 지정할 수 있음.
                                # sep='@' 로 했다면 11001100에 대한 출력은 3@1@4