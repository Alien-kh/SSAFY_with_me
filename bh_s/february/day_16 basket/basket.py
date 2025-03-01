N, M = map(int,input().split()) # N개의 바구니 및 M번 바구니의 순서를 역순으로.
baskets =[i for i in range(1, N+1)]

for _ in range(M):
    a, b = map(int, input().split()) # a번부터 b번까지 바구니를 역순
    while a < b:
        baskets[a - 1], baskets[b - 1] = baskets[b - 1], baskets[a - 1]
        a += 1
        b -= 1

print(*baskets)