testcase = int(input())
for tc in range(1, testcase +1):
    N = int(input())
    before = list(map(int,input().split()))
    after = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        if before[i]!= after[i]:
            cnt += 1
            for j in range(i, N):
                before[j]= 1- before[j]
            if before == after:
                break


    print(f'#{tc} {cnt}')