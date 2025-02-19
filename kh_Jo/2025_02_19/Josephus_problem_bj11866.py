# from collections import deque
# q = deque()
N, M = map(int, input().split()) # N 은 사람 M 은 죽이는 순서
arr = [i for i in range(1, N+1)]
# for i in range(1, N +1):
#     q.append(i)
front = 0 # 시작점
lst = [] # 죽은 사람 순서
while arr:
    front = (front + M - 1) % len(arr)
    lst.append(arr.pop(front))
print('<'+', '.join(map(str, lst)) + '>')