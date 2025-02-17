# swea, 6485 삼성시의 버스 노선

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    stops = [0] * 5001  # 1부터 5000번 정류장까지 카운트할 배열
    
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            stops[i] += 1  # 해당 범위의 정류장 카운트 증가
    
    P = int(input())
    result = ""
    
    for _ in range(P):
        C = int(input())
        result += str(stops[C]) + " "  # 정류장 C의 버스 노선 개수 추가
    
    print(f"#{test} {result.strip()}")