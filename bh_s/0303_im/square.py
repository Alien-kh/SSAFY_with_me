# 11039 사각형 찾기

# 사각형이 여러 개인 경우 곱이 가장 큰 경우를 출력.

# 1을 만나면 가로길이와 세로길이 세기.

# +a 로 가장 작은 것 출력하기도 고려해 볼 것.

# 행렬 영역중에서 가장 큰 사각형 영역을 반환하는 함수
def solve():
    # 행렬을 행 우선순회 하면서 1을 만나면 사각형의 가로길이와 세로 길이 구하기.
    max_v = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '1' :
                # 만일 최소를 구하고 싶다면 -> 좌측상단 일때만 가로길이 세로길이 구하기.
                # 위쪽과 왼쪽이 둘다 0이면 좌측상단이 시작점.
                # if (i > 0 and arr[i-1][j] == '0') and (j > 0 and arr[i][j-1] == '0')

                # 가로 길이 구하기
                # 세로 길이 구하기
                width = 0
                height = 0
                p_c = j # 현재 열 인덱스
                p_r = i
                while p_r < N and arr[i][p_c] == '1':
                    width += 1
                    p_r += 1
                
                while p_c < N and arr[p_r][j] == '1':
                    height += 1
                    p += 1

                area = width * height
                if max_v < area:
                    max_v = area
    
    return max_v

T = int(input())
for tc in range(1, T+1):
    # 2차원 배열 영역 크기
    N = int(input())
    # 한 줄 입력, 띄어쓰기 기준으로 자르고 >> N번 반복하기
    # 문자열로 입력했다.
    arr = [input().split() for _ in range(N)] 
    # 꼭 입력 확인.
    # for row in arr:
    #     print(row)

    result = solve(N, arr)
    print(f'#{tc} {result}')