# 23795 우주 괴물

# 델타로 접근해도 되고, 반복문으로 접근해도 되고!
# 이번 문제 한정으로는 반복문이 더 낫다.

# 괴물로 부터 안전한 칸 반환
def solve():
    # 괴물 위치 찾고, 상하 좌우로 while문 돌리면서 표시하기
    
    for i in range(N):
        for j in range(N):
           
            if arr[i][j] == 2:  # 괴물 찾음!!!
                r, c = i, j
                # 상하좌우 광선 표시하기
                # 현재 위치는 i, j
                while 0 <= r and arr[r][c] != 1:
                    # 광선은 문제 외의 값 ex) 3 으로 표시하자.
                    arr[r][c] = 3
                    i -= 1
                r, c = i, j
                while r < N and arr[r][c] != 1:
                    arr[r][c] = 3
                    r += 1

                r, c =i, j
                while 0 <= c and arr[r][c] != 1:
                    arr[r][c] = 3
                    c -= 1
                
                r, c =i, j
                while c < N and arr[r][c] != 1:
                    arr[r][c] = 3
                    c += 1

                cnt = 0
                # 안전한 칸 수 세기
                for k in range(N):
                    for l in range(N):
                        if arr[k][l] == 0:
                            cnt += 1

                return cnt

            
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = solve()
    print(f'#{tc} {result}')