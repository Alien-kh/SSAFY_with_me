import heapq
import sys
pq = []
N = int(sys.stdin.readline())
for i in range(N):
    x = int(sys.stdin.readline())
    
    if x ==  0:
        if len(pq) == 0:
            print(0)
        else:
            now = heapq.heappop(pq)
            print(now)
    else:       
        heapq.heappush(pq,(x))