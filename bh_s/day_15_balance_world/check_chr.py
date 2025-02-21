def check_parentheses(txt):
    """
    주어진 문자열에서 괄호의 짝이 맞는지 확인하는 함수.
    괄호가 올바르게 닫혀 있으면 'yes', 그렇지 않으면 'no' 반환.
    """
    top = -1  # 스택의 최상위 위치를 나타내는 변수
    stack = [0] * 10000  # 최대 10000개의 괄호를 저장할 수 있는 리스트를 스택으로 사용
    pair_dict = {')': '(', ']': '['}  # 소괄호와 대괄호만 허용

    ans = 'yes'  # 기본적으로 짝이 맞다고 가정
    for x in txt:
        if x in '([':  # 여는 괄호일 경우 스택에 추가 (push)
            top += 1
            stack[top] = x
        elif x in ')]':  # 닫는 괄호일 경우
            if top == -1 or stack[top] != pair_dict[x]:  # 스택이 비었거나 짝이 맞지 않으면 'no'
                ans = 'no'
                break
            else:  # 짝이 맞으면 스택에서 제거 (pop)
                top -= 1

    if top > -1:  # 스택에 여는 괄호가 남아있으면 'no'
        ans = 'no'
    return ans

# 여러 줄 입력을 받아 각 줄마다 check_parentheses를 적용한 후 한 번에 출력하는 함수
def process_lines():
    """
    여러 줄의 입력을 받아 각 줄마다 괄호 검사 수행 후 한 번에 결과 출력.
    마지막 입력이 단독 온점('.')이면 종료.
    """
    lines = []  # 결과를 저장할 리스트
    while True:
        try:
            line = input().rstrip()  # 입력을 받고 오른쪽 공백 제거
            if line == '.':  # 마지막 입력이 단독 온점이면 종료
                break
            if len(line) >= 100 or not line.endswith('.'):  # 입력 조건에 맞지 않으면 무시
                continue
            lines.append(check_parentheses(line[:-1]))  # 마지막 온점 제외하고 검사 후 결과를 리스트에 추가
        except EOFError:
            break  # EOF 발생 시 입력 종료
    print('\n'.join(lines))  # 모든 결과를 한 번에 출력

# 함수 실행
process_lines()