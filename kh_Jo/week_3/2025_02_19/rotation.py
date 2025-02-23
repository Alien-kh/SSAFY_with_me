from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N개의 숫자,  뒤로 보내는 작업 M번
    arr = list(map(int, input().split()))
    front = 0 # 현재 idx
    # 맨 뒤로 보내는 작업은 앞에서 맨뒤어 넘기거나 가리키는 front를 한 칸 씩 돌려주면 되는 것 아닌가?
    front = (front + M) % N
    print(f'#{tc} {arr[front]}')
    # q= deque()
    # for num in arr:
    #     q.append(num)
    # for _ in range(M):
    #     a = q.popleft()
    #     q.append(a)
    # result = q.popleft()
    # print(f'#{tc} {result}')