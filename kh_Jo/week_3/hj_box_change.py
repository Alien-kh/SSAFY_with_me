T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0] * N
    for i in range(1, Q+1):
        l, R = map(int, input().split())
        l -= 1 # 1번째 박스는 0번째 idx
        for j in range(l, R): # l번째 박스부터부터 R 박스까지 바꿔주기
            arr[j] = i

    print(f'#{tc}',*arr) # 결과 출력

