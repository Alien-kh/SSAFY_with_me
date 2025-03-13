# N = int(input())
# queue = [0] * N
# for i in range(N):
#     queue[i] = N - i
#
# while len(queue) > 1:
#     queue.pop()
#     queue.append(queue.pop(0))
#
# print(queue[0])

from collections import deque

N = int(input())
queue = deque(range(1, N+1))

while len(queue) > 1:
    queue.popleft()  # 첫 번째 카드 버림
    queue.append(queue.popleft())  # 두 번째 카드를 맨 뒤로 이동

print(queue[0])
