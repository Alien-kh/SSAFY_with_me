# 연립방정식 ax + by = c / dx + ey = f 에서 a~f 까지 한 줄에 공백을 기준으로 구분해서 주어짐

# 내가 생각한 방식(진짜 무식한 경우) 이 경우 분모가 0 인 상황이 발생.
a, b, c, d, e, f = map(int, input().split())
y = int((d*c - a*f) / (b*d - a*e))
x = int((c-b*y) / a)
print(f'{x} {y}')

# 진짜 브루트포스 방식
a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)     # 너무 어렵게 생각했다. 애초에 x,y에 대하여 조건문을 주면 자동적으로 x,y를 찾을 수 있음.
            exit()  # x,y를 찾았으면 더 이상 진행할 필요 x