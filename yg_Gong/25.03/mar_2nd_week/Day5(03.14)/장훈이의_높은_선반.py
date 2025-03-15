# 점원들로 탑을 쌓아서 선반높이에 도달하게 만들것
# 만들 수 있는 탑의 높이중에
# 선반보다 같거나 높으면서 그중에 제일낮은 탑의 높이를 찾기
# 제일 낮은 높이에서 선반높이의 차를 출력
# import sys
# sys.stdin = open('input.txt')

def shelf(idx, sum_tall):
    global min_top
    if idx == N:    # idx가 점원수를 넘어가지 않도록
        if sum_tall >= B:
            if sum_tall < min_top:
                min_top = sum_tall
        return

    # 현재 요소를 포함
    shelf(idx + 1, sum_tall + tall[idx])
    # 현재 요소를 미포함
    shelf(idx + 1, sum_tall)



T = int(input())
for tc in range(1, T + 1):
    N,B = map(int, input().split()) # N:점원 수 , B: 선반높이
    tall = list(map(int, input().split()))
    min_top = 0xffffffff
    shelf(0,0)
    result = min_top - B

    print(f'#{tc} {result}')