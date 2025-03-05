
T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        a,b = map(int,input().split())
        tree[a] = b

    i = 1
    while not tree[L]:
        if i * 2 > N:
            i = 1
            continue
        elif i*2 +1 > N:
            tree[i] = tree[i*2]
        if not tree[i] and tree[(i * 2)] and tree[(i*2)+1]:
            tree[i] = tree[(i * 2)] + tree[(i*2) + 1]
            i = 1
        else:
            i+=1



    print(f'#{tc} {tree[L]}')
