def solve(d):
    code_lst = []
    for i in range(0, len(d), 7):   # 7자리씩 자르기.
        code =''.join(map(str, d[i:i+7]))
        code_lst.append(code)   # 자른 코드를 lst에 넣기. (문자열로)

    result = []
    for cd in code_lst:     # code_lst 에 있는 7자리씩 자른 코드 하나씩 가져오기
        value_ten = 0       # 10진수 저장 변수 (하나의 코드가 끝나면 다시 0이 된다)
        for j in range(7):  # 주의. 내가 넣은 코드의 인덱스와 자리수는 반대다.
            value_ten += int(cd[j]) * (2 ** (6 - j))
        result.append(str(value_ten))

    print(' '.join(result))     # 이어붙이기


data = list(map(int, input().strip()))
solve(data)
