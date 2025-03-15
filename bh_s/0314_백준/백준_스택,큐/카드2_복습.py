from collections import deque

N = int(input())
queue = deque(range(1, N + 1))

while len(queue) > 1:   # 크기가 1이 될 때 까지.
    queue.popleft()  # 첫 번째 카드 버리고
    queue.append(queue.popleft())   # 2번째 카드 버림과 동시에 맨 끝에 넣기.

print(queue[0])
