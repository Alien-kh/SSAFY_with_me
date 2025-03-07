# 세 점이 주어졌을 때, 축에 평행한 사각형 만들기

def solve(d):

    if d[0][0] == d[1][0]:
        x = d[2][0]
    elif d[1][0] == d[2][0]:
        x = d[0][0]
    else:
        x = d[1][0]

    if d[0][1] == d[1][1]:
        y = d[2][1]
    elif d[1][1] == d[2][1]:
        y = d[0][1]
    else:
        y = d[1][1]

    return x, y


data = [list(map(int, input().split())) for _ in range(3)]

# 조건문 -> 각 값들이 같으면 남은 하나의 값이 평행한 사각형의 좌표가 된다.

result_x, result_y = solve(data)
print(f'{result_x} {result_y}')
