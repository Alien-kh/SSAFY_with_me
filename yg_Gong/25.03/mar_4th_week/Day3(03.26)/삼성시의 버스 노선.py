# 버스정류장 갯수 크기와 같은 배열 생성(50001)
# A~B범위에 해당하는 버스정류장에  +1 씩
# 노선을 다 돌면 P에해당하는 노선과 같은 인덱스의 배열값을 출력

T = int(input())

for tc in range(1, T+1):
    bus_stop = [0] * 5001   # 버스정류장은 1~5000번 -> 0번인덱스는 안씀
    N = int(input())    # 버스 노선 갯수
    for _ in range(N):
        A,B = map(int, input().split())
        for i in range(A, B+1):
            bus_stop[i] += 1    # A~B 버스정류장에 +1씩
    P = int(input())
    print(f'#{tc}',end=' ')
    for _ in range(P):
       C = int(input()) # 버스정류장 번호
       print(bus_stop[C], end=' ')


    print()


