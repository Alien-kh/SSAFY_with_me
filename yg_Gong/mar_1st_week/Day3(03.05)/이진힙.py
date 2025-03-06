# heap 생성 함수
def heappush(heap, data):

    heap.append(data)
    current = len(heap) - 1
    parent = (current - 1) // 2

    while current > 0 and heap[current] < heap[parent]:
        heap[current], heap[parent] = heap[parent], heap[current]
        current = parent
        parent = (current - 1) // 2

# 노드값 합산 함수
def get_parent_sum(heap, idx):
    total = 0
    while idx > 0:
        idx = (idx - 1) // 2  # 부모 노드로 이동
        total += heap[idx]  # 부모 노드의 값 더하기
    return total


T = int(input().strip())  # 테스트 케이스 개수
results = []

for tc in range(1, T + 1):
    N = int(input().strip())  # 배열 크기
    numbers = list(map(int, input().split()))  # N개의 숫자 입력

    heap = []
    for num in numbers:
        heappush(heap, num)  # 최소 힙에 삽입

    last_index = len(heap) - 1  # 마지막 노드의 인덱스
    parent_sum = get_parent_sum(heap, last_index)  # 노드 합 계산

    print(f"#{tc} {parent_sum}")

