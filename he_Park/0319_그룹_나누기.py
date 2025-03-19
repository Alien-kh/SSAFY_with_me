def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]  # 경로 압축
        x = parents[x]
    return x


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x > ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


T = int(input())
for tc in range(1, T + 1):

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parents = [i for i in range(N + 1)]

    for i in range(0, 2*M, 2):
        union(arr[i], arr[i+1])

    # parents를 최상단 노드로 바꿔야 한다
    for j in range(1, N + 1):
        parents[j] = find_set(j)

    print(f'#{tc} {len(set(parents)) - 1}')  # 0 뺴고 길이 출력


    ''' 마지막에 parents를 최상단 노드로 바꿔야 하는 이유
    5 4
    2 5 5 4 4 1 4 2
    '''