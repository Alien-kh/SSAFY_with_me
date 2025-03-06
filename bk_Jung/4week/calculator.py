def postorder(v):
    if v is None:  # 노드가 없으면 리턴
        return

    # 왼쪽 서브트리 방문
    postorder(left[v])
    # 오른쪽 서브트리 방문
    postorder(right[v])

    # 현재 노드가 연산자인지 숫자인지 확인
    if tree[v] in "+-*/":
        b = stack.pop()
        a = stack.pop()
        if tree[v] == '+':
            stack.append(a + b)
        elif tree[v] == '-':
            stack.append(a - b)
        elif tree[v] == '*':
            stack.append(a * b)
        elif tree[v] == '/':
            stack.append(a / b)  # 나눗셈 결과는 float
    else:
        stack.append(int(tree[v]))  # 숫자는 스택에 저장


T = 10  # 테스트 케이스 개수
for tc in range(1, T + 1):
    N = int(input())  # 노드 개수
    left = [None] * (N + 1)
    right = [None] * (N + 1)
    tree = [None] * (N + 1)

    for i in range(N):
        arr = input().split()
        a = int(arr[0])  # 노드 번호
        b = arr[1]  # 노드 값 (숫자 또는 연산자)
        tree[a] = b  # 트리에 저장

        if len(arr) > 2:
            left[a] = int(arr[2])  # 왼쪽 자식 노드 번호
        if len(arr) > 3:
            right[a] = int(arr[3])  # 오른쪽 자식 노드 번호

    stack = []
    postorder(1)  # 루트(1번 노드)에서 후위 순회 실행
    print(f'#{tc} {int(stack.pop())}')  # 계산 결과 출력
