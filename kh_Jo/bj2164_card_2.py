import sys
from collections import deque

N = int(sys.stdin.readline()) # 그냥 input으로 하니깐 런타임 에러
q = deque(range(1, N + 1)) # 이렇게 하면 q에 값을 넣을 수 있다.

while len(q) > 1:
    q.popleft()            # 맨 위의 카드 버리기
    q.append(q.popleft())  # 그 다음 카드를 맨 아래로 이동

print(q[0])
