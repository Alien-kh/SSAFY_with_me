def hex_to_bin(d):
    code_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
        '6': '0110', '7': '0111', '8': '1000', '9': '1001',
        'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    # 리스트가 아니라 문자열을 합쳐서 반환
    return ''.join(code_map[cd] for cd in d)


def solve_bin(d):
    code_lst = []
    for i in range(0, len(d), 7):  # 7자리씩 자르기.
        code = d[i:i + 7]  # 문자열 그대로 슬라이싱
        code_lst.append(code)  # 자른 코드를 lst에 넣기. (문자열로)

    result = []
    for cd in code_lst:  # code_lst 에 있는 7자리씩 자른 코드 하나씩 가져오기
        value_ten = 0  # 10진수 저장 변수 (하나의 코드가 끝나면 다시 0이 된다)
        for j in range(len(cd)):  # 마지막 조각이 7자리가 아닐 수도 있음
            value_ten += int(cd[j]) * (2 ** (len(cd) - 1 - j))  # 자리수 계산 반대로
        result.append(str(value_ten))

    print(' '.join(result))  # 이어붙이기


data = list(input().strip())
solve_bin(hex_to_bin(data))