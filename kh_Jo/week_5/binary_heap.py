def heappush(data):
    global heapcount
    heapcount +=1
    heap[heapcount] = data
    current = heapcount
    parent = current // 2
    while True:
        if current ==1 or heap[current] > heap[parent]: # 만약 1개이거나, 부모 보다 클 떄는
            break
        if heap[current] < heap[parent]: # 부모보다 작을 때는 바꿔주기
            heap[current], heap[parent] = heap[parent], heap[current]
        current = parent
        parent = current //2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) # 일단 리스트에 다 넣어주고
    heap = [0] * (N+1)
    heapcount = 0
    for node_num in arr:
        heappush(node_num) # 리스트 안에 있는 숫자 다 넣어주기
    # 마지막 노드 찾아주기
    last_node = heap[heapcount]
    sum_anc = 0
    current = heapcount //2
    while current >0 :
        sum_anc += heap[current]
        current //= 2 # 부모로 다시 바꿔주기
    print(f'#{tc} {sum_anc}')

'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''