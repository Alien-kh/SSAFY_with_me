# subtree
def pre_order(T):  # 전위순회
    global cnt
    if T:
        cnt += 1
        # print(T, cnt)  # visit(T)  T에서 할 일 처리
        pre_order(left[T])
        pre_order(right[T])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    # E개의 부모 자식 노드 번호 쌍
    data = list(map(int, input().split()))
    left = [0] * (E + 2)  # 노드의 개수 = E+1이므로 E+1번 인덱스까지 필요하다.
    right = [0] * (E + 2)
    cnt = 0
    for i in range(0, len(data), 2):  # 부모 노드를 인덱스로 자식 노드를 저장
        if left[data[i]] == 0:
            left[data[i]] = data[i+1]
        else:
            right[data[i]] = data[i+1]

    pre_order(N)
    print(f'#{tc} {cnt}')