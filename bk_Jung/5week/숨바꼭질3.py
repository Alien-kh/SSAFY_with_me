import heapq

def dijkstra(start):
    pq = []
    heapq.heappush(pq,(0,start))
    distance[start] = 0

    while pq:
        dist,now = heapq.heappop(pq)

        if distance[now] < dist:
            continue
        if now * 2 < 100001:
            cost1 = dist
            if cost1 < distance[now*2]:
                distance[now*2] = cost1
                heapq.heappush(pq,(cost1,now*2))

        if now + 1 < 100001:
            cost2 = dist + 1
            if cost2 < distance[now + 1]:
                distance[now + 1] = cost2
                heapq.heappush(pq,(cost2,now+1))

        if now - 1 >= 0:
            cost3 = dist + 1
            if cost3 < distance[now - 1]:
                distance[now - 1] = cost3
                heapq.heappush(pq,(cost3,now-1))
    print(distance[K])


N,K = map(int,input().split())

distance = [21e8] * 100001

dijkstra(N)
