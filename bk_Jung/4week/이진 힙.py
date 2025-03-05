

def heappush(data):
    global heapcount
    # 1. 완전이진트리의 마지막에 요소 추가
    # 2. 부모요소랑 값 비교 하면서 자리 바꿔주기 * 반복
    # (루트 또는 부모가 더 클떄 까지)
    heapcount += 1
    heap[heapcount] = data
    current = heapcount
    parent = current // 2
    while True:
        if current == 1 or heap[current] > heap[parent]:
            break
        if heap[current] < heap[parent]:
            heap[current], heap[parent] = heap[parent], heap[current]
        current = parent
        parent = current // 2

T = int(input())

for tc in range(1,T+1):
    heap = [0] * 1000000
    heapcount = 0

    N = int(input())
    arr = list(map(int,input().split()))

    for i in arr:
        heappush(i)

    result = 0
    now = N
    while True:
        if now % 2 == 0:
            now //= 2
        else:
            now -= 1
            now //= 2
        if heap[now]:
            result += heap[now]
        else:
            break

    print(f'#{tc} {result}')