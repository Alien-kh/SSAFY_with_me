def make_set(n):
    # 1~n 까지의 원소가 있다고 가정 -> 총 n 개의 집합을 생성
    # --> 각 원소의 부모(!= 대표자)를 자신으로 초기화
    parents = [i for i in range(n + 1)]
    # ranks = [0] * (n + 1)  # rank 를 모두 0으로 초기화
    return parents

def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]  # 경로 압축
        x = parents[x]
    return x
# print('경호 존잘존멋')
def union(x, y):
    # 1. x, y 의 대표자를 검색
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 만약 이미 같은 집합이라면 ?
    # -> 끝!
    if ref_x == ref_y:
        return

    # 다른 집합이라면 합친다

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) #  N은 출석번호, M 장의 신천서
    parents = make_set(N)
    arr = list(map(int,input().split()))
    # print(parents)
    for i in range(M):
        union(arr[i*2], arr[i*2+1])
    # print(parents)
    # result = len(set(parents)) -1 # 0번 뺴주기
    result = len({find_set(i) for i in range(1, N+1)})

    print(f'#{tc} {result}')