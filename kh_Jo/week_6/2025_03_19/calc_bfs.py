

def bfs(v,cnt):


    q=[]
    set_1 = set()# set을 만들어서 같은 수가 나오면 넘어감

    q.append((v, cnt))
    while q:
        curr, curr_cnt = q.pop(0)

        if curr in set_1: # 만약에 이미 나온 숫자면 볼 필요 없이 넘어감
            continue

        if curr == N:
            return curr_cnt
        set_1.add(curr)
        q.append((curr-1, curr_cnt+1))
        q.append((curr+1, curr_cnt+1))
        if curr % 2==0:
            q.append((int(curr/2), curr_cnt+1))
        q.append((curr+10, curr_cnt+1))
    return -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    result = bfs(M,0)
    print(f'#{tc} {result}')