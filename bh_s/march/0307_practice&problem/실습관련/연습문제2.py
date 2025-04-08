# 연습문제 2. 1이 2진수였다면 이번것은 16진수다.

def hex_to_bin(d):  # 16진수를 딕셔너리로 이용해서 이진수 이어붙이기
    code_map = {
        '0' : '0000' , '1' : '0001', '2' : '0010', '3' : '0011', '4' : '0100', '5' : '0101',
        '6' : '0110' , '7' : '0111', '8' : '1000', '9' : '1001',
        'A' : '1010' , 'B' : '1011', 'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111'
    }
    binary_code =''     # 이진수 코드로 저장 할 변수
    for cd in d:        # 입력한 d(data) 리스트의 요소를 각각 2진수로 만들기.
        binary_code += code_map[cd]

    return binary_code  # 이진수 코드 반환 -> 문제 1에서 만든 함수(일부 수정)에 바로 넣어주기 위해서.


def solve_bin(d):
    code_lst = []
    for i in range(0, len(d), 7):   # 7자리씩 자르기.
        code = ''.join(map(str, d[i:i+7]))
        code_lst.append(code)   # 자른 코드를 lst에 넣기. (문자열로)

    result = []
    for cd in code_lst:     # code_lst 에 있는 7자리씩 자른 코드 하나씩 가져오기
        value_ten = 0       # 10진수 저장 변수 (하나의 코드가 끝나면 다시 0이 된다)
        for j in range(len(cd)):  # 주의. 내가 넣은 코드의 인덱스와 자리수는 반대다. + 예시 입력을 보면 마지막은 7자리가 아니다.
            value_ten += int(cd[j]) * (2 ** (len(cd) - 1 - j))
        result.append(str(value_ten))

    print(' '.join(result))     # 이어붙이기


data = list(input().strip())
solve_bin(hex_to_bin(data))
