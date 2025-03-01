T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_length = 0
    
    # 가로로 연속된 구조물 탐색
    for r in range(N):
        length = 0
        for c in range(M):
            if data[r][c] == 1:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 0
        max_length = max(max_length, length) 

    # 세로로 연속된 구조물 탐색
    for c in range(M):
        length = 0
        for r in range(N):
            if data[r][c] == 1:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 0
        max_length = max(max_length, length)  
        
    print(f"#{test} {max_length}")