# 균형잡힌 세상
def delete_parentheses(arr):
    stack = []
    for i in arr:
        # 여는 괄호는 스택에 추가
        if i in "([":
            stack.append(i)
        # 닫는 괄호를 만나면 스택이 비어있는지 먼저 체크
        elif i == ')':
            if not stack or stack[-1] != '(':  # 스택이 비었거나 짝이 안 맞으면
                return "no"
            stack.pop()  # 짝이 맞으면 pop()
        elif i == ']':
            if not stack or stack[-1] != '[':  # 스택이 비었거나 짝이 안 맞으면
                return "no"
            stack.pop()  # 짝이 맞으면 pop()

    # 스택이 비어 있으면 짝이 맞음 -> "yes" 반환, 남아 있으면 "no" 반환
    return "yes" if not stack else "no"

while True:
    arr = input().rstrip()
    if arr == ".":  # 종료 조건
        break
    result = delete_parentheses(arr)
    print(result)
