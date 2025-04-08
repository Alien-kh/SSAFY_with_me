N = int(input())  # 입력 개수
c_cnt = 0

while c_cnt < N:
    data = input()
    stack = []  # 매번 새로운 스택 초기화
    is_valid = True

    for char in data:
        if char == '(':
            stack.append(char)
        else:
            if not stack:  # 스택이 비었으면 올바른 괄호쌍이 아님
                is_valid = False
                break
            stack.pop()  # 올바른 경우 스택에서 '(' 제거

    # 결과 출력
    if is_valid and not stack:
        print('YES')
    else:
        print('NO')

    c_cnt += 1