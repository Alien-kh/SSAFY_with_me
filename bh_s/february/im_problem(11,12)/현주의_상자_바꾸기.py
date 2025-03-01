T = int(input())

for tc in range(1,T+1):
    N, Q = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(Q)]
    boxes = [0] * N

    for i in range(Q):
        L, R = data[i]
        for j in range(L-1, R):
            boxes[j] = i + 1

    print(f"#{tc}", *boxes)