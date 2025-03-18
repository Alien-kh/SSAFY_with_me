# 전위, 중위, 후위 순회 구현
def preorder(tree, idx, result):
    if idx >= len(tree):  # 노드가 존재하지 않으면 종료
        return
    result.append(tree[idx])  # 루트 노드 먼저 방문
    preorder(tree, 2*idx + 1, result)  # 왼쪽 자식 방문
    preorder(tree, 2*idx + 2, result)  # 오른쪽 자식 방문


def inorder(tree, idx, result):
    if idx >= len(tree):  # 노드가 존재하지 않으면 종료
        return
    inorder(tree, 2*idx + 1, result)  # 왼쪽 자식 방문
    result.append(tree[idx])  # 루트 노드 방문
    inorder(tree, 2*idx + 2, result)  # 오른쪽 자식 방문


def postorder(tree, idx, result):
    if idx >= len(tree):  # 노드가 존재하지 않으면 종료
        return
    postorder(tree, 2*idx + 1, result)  # 왼쪽 자식 방문
    postorder(tree, 2*idx + 2, result)  # 오른쪽 자식 방문
    result.append(tree[idx])  # 루트 노드 방문


# 10진수 계산 함수
def calculate(arr):
    arr = arr[::-1]  # 이진수에서 뒤집어서 계산해야 하므로
    value = 0
    for i in range(len(arr)):
        value += arr[i] * 2**i
    return value


# 테스트 코드
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 트리의 노드 개수
    data = list(map(int, input().split()))  # 트리의 데이터

    # 트리의 인덱스를 0부터 N-1까지 설정
    tree = data

    # 전위, 중위, 후위 순회 결과 리스트
    preorder_result = []
    inorder_result = []
    postorder_result = []

    # 순회 함수 호출
    preorder(tree, 0, preorder_result)
    inorder(tree, 0, inorder_result)
    postorder(tree, 0, postorder_result)

    # 각 순회 결과로 10진수 계산
    c_value1 = calculate(preorder_result)
    c_value2 = calculate(inorder_result)
    c_value3 = calculate(postorder_result)

    # 최대값을 출력
    result = max(c_value1, c_value2, c_value3)
    print(f'#{tc} {result}')
