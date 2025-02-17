N, M = map(int, (input().split()))
lst = list(map(int,input().split()))

max_v = -21e8
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if lst[i] + lst[j] + lst[k] <= M:
                max_v = max(max_v, lst[i] + lst[j] + lst[k])
            else:
                continue

print(max_v)