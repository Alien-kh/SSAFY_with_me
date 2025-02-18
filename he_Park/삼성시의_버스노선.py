T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    # arr[][0] : A1  arr[][1] : B1
    P = int(input())
    counts = [0] * (5000+1)  # 인덱스 번호랑 정류장 번호랑 맞춰줌
    Cj = [int(input()) for _ in range(P)]  # 정류장 번호

    for i in range(N):
        for j in range(arr[i][0], arr[i][1] + 1):  # A1부터 B1까지
          counts[j] += 1
    print(f'#{tc}', end=" ")
    for k in Cj:
        print(counts[k], end = " ")

    print()  # 이 패턴 걍 외우는 걸로,,